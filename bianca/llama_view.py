from bianca.bootstrap import *

import hashlib
import keyword
from pathlib import Path
from collections import deque

from clang.cindex import CursorKind, Index, TypeKind

__all__ = []


def get_py_type_hint(ctype_str: str, is_helper: bool = False, defined_structs: set = None) -> str:
    if defined_structs is None:
        defined_structs = set()

    c_int_types = ["int8", "uint8", "int16", "uint16", "int32", "uint32", "int64", "uint64", "int", "uint", "size_t"]
    c_int_types = [f"ctypes.c_{it}" for it in c_int_types]

    if ctype_str == "None":
        return "None"
    if ctype_str == "ctypes.c_bool":
        return "bool"
    if ctype_str in c_int_types:
        return "int"
    if ctype_str in ["ctypes.c_float", "ctypes.c_double"]:
        return "float"
    if ctype_str in ["ctypes.c_char", "ctypes.c_char_p"]:
        return "bytes"
    if ctype_str == "ctypes.c_void_p":
        return "Any"
    if ctype_str.startswith("ctypes.POINTER("):
        return "Any"
    if ctype_str.startswith("("):
        return "Any"

    if is_helper and ctype_str in defined_structs:
        return f"'Py{ctype_str}'"

    if not ctype_str.startswith("ctypes."):
        return f"'{ctype_str}'"

    return f"'{ctype_str}'"


PRIMITIVES = {
    "void": "None",
    "bool": "ctypes.c_bool",
    "int8_t": "ctypes.c_int8",
    "uint8_t": "ctypes.c_uint8",
    "int16_t": "ctypes.c_int16",
    "uint16_t": "ctypes.c_uint16",
    "int32_t": "ctypes.c_int32",
    "uint32_t": "ctypes.c_uint32",
    "int64_t": "ctypes.c_int64",
    "uint64_t": "ctypes.c_uint64",
    "int": "ctypes.c_int",
    "unsigned int": "ctypes.c_uint",
    "size_t": "ctypes.c_size_t",
    "float": "ctypes.c_float",
    "double": "ctypes.c_double",
    "char": "ctypes.c_char",
}


def snake_to_camel_case(snake_str: str) -> str:
    return "".join(it.title() for it in snake_str.split('_'))


def get_struct_name(spelling: str) -> str:
    if not spelling:
        return "Unnamed_00000000"
    if "(unnamed at" in spelling.lower():
        return f"Unnamed_{hashlib.md5(spelling.encode()).hexdigest()[:8]}"
    return snake_to_camel_case(spelling.replace("struct ", "").strip())


def apply_pointers(base_type: str, num_stars: int) -> str:
    res = base_type
    for _ in range(num_stars):
        if res == "None":
            res = "ctypes.c_void_p"
        elif res == "ctypes.c_char":
            res = "ctypes.c_char_p"
        else:
            res = f"ctypes.POINTER({res})"
    return res


def resolve_type(c_type, opaque_pointers_tracker, deps) -> str:
    spelling = c_type.spelling.replace("const ", "").replace("volatile ", "").strip()

    if spelling in PRIMITIVES:
        return PRIMITIVES[spelling]

    if c_type.kind == TypeKind.CONSTANTARRAY:
        elem_type = resolve_type(c_type.get_array_element_type(), opaque_pointers_tracker, deps)
        size = c_type.get_array_size()
        return f"({elem_type} * {size})"

    if c_type.kind == TypeKind.INCOMPLETEARRAY:
        elem_type = resolve_type(c_type.get_array_element_type(), opaque_pointers_tracker, deps)
        if elem_type == "ctypes.c_char":
            return "ctypes.c_char_p"
        return f"ctypes.POINTER({elem_type})"

    if c_type.kind == TypeKind.POINTER:
        pointee = c_type.get_pointee()
        p_spelling = pointee.spelling.replace("const ", "").replace("volatile ", "").strip()

        if p_spelling == "char":
            return "ctypes.c_char_p"
        if p_spelling == "void":
            return "ctypes.c_void_p"

        base_cursor = c_type
        num_stars = 0
        while base_cursor.kind == TypeKind.POINTER:
            base_cursor = base_cursor.get_pointee()
            num_stars += 1

        if pointee.kind in (TypeKind.UNEXPOSED, TypeKind.FUNCTIONPROTO) or base_cursor.kind in (TypeKind.UNEXPOSED,
                                                                                                TypeKind.FUNCTIONPROTO):
            return apply_pointers("ctypes.c_void_p", max(0, num_stars - 1))

        base_spelling = base_cursor.spelling.replace("const ", "").replace("volatile ", "").strip()

        if base_spelling.startswith("struct llama_") or base_spelling.startswith("llama_"):
            base_name = base_spelling.replace("struct ", "").strip()
            struct_name = snake_to_camel_case(base_name)
            ptr_name = struct_name + "Pointer"

            opaque_pointers_tracker.add(ptr_name)
            deps.add(ptr_name)
            deps.add(struct_name)
            return apply_pointers(ptr_name, num_stars - 1)

        base_ctypes = resolve_type(base_cursor, opaque_pointers_tracker, deps)
        if base_ctypes == "None":
            base_ctypes = "ctypes.c_void_p"
        return apply_pointers(base_ctypes, num_stars)

    if c_type.kind == TypeKind.ENUM or spelling.startswith("enum "):
        return "ctypes.c_int32"

    if c_type.kind == TypeKind.RECORD or spelling.startswith("struct "):
        struct_name = get_struct_name(spelling)
        deps.add(struct_name)
        return struct_name

    if c_type.kind == TypeKind.TYPEDEF:
        canonical = c_type.get_canonical()
        if canonical.kind != TypeKind.TYPEDEF:
            return resolve_type(canonical, opaque_pointers_tracker, deps)

    return "ctypes.c_void_p"


def generate_bindings():
    python_builtins = [
        "abs", "aiter", "all", "anext", "any", "ascii", "bin", "bool",
        "breakpoint", "bytearray", "bytes", "callable", "chr", "classmethod",
        "compile", "complex", "delattr", "dict", "dir", "divmod", "enumerate",
        "eval", "exec", "filter", "float", "format", "frozenset", "getattr",
        "globals", "hasattr", "hash", "help", "hex", "id", "input", "int",
        "isinstance", "issubclass", "iter", "len", "list", "locals", "map",
        "max", "memoryview", "min", "next", "object", "oct", "open", "ord",
        "pow", "print", "property", "range", "repr", "reversed", "round",
        "set", "setattr", "slice", "sorted", "staticmethod", "str", "sum",
        "super", "tuple", "type", "vars", "zip"
    ]

    translation_unit = Index.create().parse(str(LLAMA_HEADER), args=['-x', 'c', '-std=c11'])

    structs = {}
    functions = []
    opaque_pointers = set()

    llama_roots = set()
    struct_deps_map = {}

    for cursor in translation_unit.cursor.walk_preorder():
        in_llama = cursor.location.file and Path(cursor.location.file.name) == Path(LLAMA_HEADER)

        if cursor.kind == CursorKind.STRUCT_DECL and cursor.is_definition():
            struct_name = get_struct_name(cursor.spelling or cursor.type.spelling)
            fields = []
            deps = set()

            for child in cursor.get_children():
                if child.kind == CursorKind.FIELD_DECL:
                    f_name = child.spelling
                    f_type = resolve_type(child.type, opaque_pointers, deps)
                    fields.append((f_name, f_type))

            structs[struct_name] = fields
            struct_deps_map[struct_name] = deps
            if in_llama:
                llama_roots.add(struct_name)

        elif cursor.kind == CursorKind.FUNCTION_DECL:
            func_name = cursor.spelling
            deps = set()
            restype = resolve_type(cursor.result_type, opaque_pointers, deps)

            args = []
            for arg in cursor.get_arguments():
                arg_name = arg.spelling
                if not arg_name:
                    s = arg.type.spelling.replace("const ", "").replace("volatile ", "").replace("struct ", "").strip()
                    arg_name = s.replace(" *", "_ptr").replace("*", "_ptr").replace(" ", "_")
                if keyword.iskeyword(arg_name) or arg_name in python_builtins:
                    arg_name = arg_name + "_"
                args.append((arg_name, resolve_type(arg.type, opaque_pointers, deps)))

            functions.append((func_name, restype, args))
            if in_llama:
                llama_roots.add(func_name)
                llama_roots.update(deps)

    required_symbols = set(llama_roots)
    queue = deque(llama_roots)
    while queue:
        sym = queue.popleft()
        if sym in struct_deps_map:
            for d in struct_deps_map[sym]:
                if d not in required_symbols:
                    required_symbols.add(d)
                    queue.append(d)

    structs = {k: v for k, v in structs.items() if k in required_symbols}
    functions = [f for f in functions if f[0] in required_symbols]
    opaque_pointers = {p for p in opaque_pointers if p in required_symbols}

    defined_struct_names = set(structs.keys())
    function_names = {f[0] for f in functions}
    opaque_structs = required_symbols - defined_struct_names - function_names - opaque_pointers

    all_exports = []
    for s in structs.keys():
        all_exports.append(f'"{s}"')
        all_exports.append(f'"Py{s}"')
    for p in opaque_pointers: all_exports.append(f'"{p}"')
    for func_name, _, _ in functions:
        all_exports.extend([f'"c_{func_name}"', f'"{func_name}"'])

    print("from bianca.bootstrap import *")
    print()

    print("__all__ = [")
    for exp in all_exports:
        print(f"    {exp},")
    print("]")
    print()

    print("llama = ctypes.CDLL(LLAMA_LIB)\n")

    for o_struct in sorted(opaque_structs):
        print(f"class {o_struct}(ctypes.Structure):")
        print("    pass")
        print()

    for struct_name, fields in structs.items():
        print(f"class {struct_name}(ctypes.Structure):")
        print("    @property")
        print(f"    def py(self) -> 'Py{struct_name}':")
        print(f"        return Py{struct_name}(")
        for f_name, f_type in fields:
            if f_type in structs:
                print(f"            {f_name}=self.{f_name}.py,")
            else:
                print(f"            {f_name}=self.{f_name},")
        print("        )")
        print()
        print("    @py.setter")
        print(f"    def py(self, value: 'Py{struct_name}'):")
        for f_name, f_type in fields:
            print(f"        setattr(self, \"{f_name}\", value.c.{f_name})")
        print()

    for ptr in sorted(opaque_pointers):
        base_struct = ptr.replace("Pointer", "")
        if base_struct in structs:
            print(f"{ptr} = ctypes.POINTER({base_struct})")
        else:
            print(f"{ptr} = ctypes.c_void_p")
    print()

    for struct_name, fields in structs.items():
        print(f"{struct_name}._fields_ = [")
        for f_name, f_type in fields:
            print(f"    (\"{f_name}\", {f_type}),")
        print("]")
        print()

    for func_name, restype, args in functions:
        arg_types = [a[1] for a in args]
        print(f"llama.{func_name}.argtypes = [{', '.join(arg_types)}]")
        print(f"llama.{func_name}.restype = {restype}\n")

    for struct_name, fields in structs.items():
        print(f"class Py{struct_name}:")
        init_args = ["self"] + [f"{f_name}=None" for f_name, _ in fields]
        print(f"    def __init__({', '.join(init_args)}):")
        if not fields:
            print("        pass")
        for f_name, _ in fields:
            print(f"        self.{f_name} = {f_name}")
        print()
        print("    @property")
        print(f"    def c(self) -> '{struct_name}':")
        print(f"        c_obj = {struct_name}()")
        for f_name, f_type in fields:
            if f_type in structs:
                print(f"        if self.{f_name} is not None:")
                print(f"            c_obj.{f_name} = self.{f_name}.c")
            else:
                print(f"        if self.{f_name} is not None:")
                print(f"            c_obj.{f_name} = self.{f_name}")
        print("        return c_obj")
        print()
        print("    @c.setter")
        print(f"    def c(self, value: '{struct_name}'):")
        print(f"        py_obj = value.py")
        for f_name, _ in fields:
            print(f"        self.{f_name} = py_obj.{f_name}")
        print()

    defined_struct_keys = set(structs.keys())

    for func_name, restype, args in functions:
        c_args_str = []
        for arg_name, arg_type in args:
            arg_hint = get_py_type_hint(arg_type, False, defined_struct_keys)
            if arg_hint == "Any":
                c_args_str.append(arg_name)
            else:
                c_args_str.append(f"{arg_name}: {arg_hint}")
        c_args_str = ", ".join(c_args_str)
        c_res_str = get_py_type_hint(restype, False, defined_struct_keys)

        if c_res_str == "None":
            print(f"def c_{func_name}({c_args_str}):")
        else:
            print(f"def c_{func_name}({c_args_str}) -> {c_res_str}:")
        print(f"    return llama.{func_name}({', '.join(name for name, _ in args)})\n")

        args_str = []
        for arg_name, arg_type in args:
            arg_hint = get_py_type_hint(arg_type, True, defined_struct_keys)
            if arg_hint == "Any":
                args_str.append(arg_name)
            else:
                args_str.append(f"{arg_name}: {arg_hint}")
        args_str = ", ".join(args_str)
        res_str = get_py_type_hint(restype, True, defined_struct_keys)

        c_params_str = ', '.join(f"{name}.c" if ctype in structs else f"{name}" for name, ctype in args)

        if res_str == "None":
            print(f"def {func_name}({args_str}):")
        else:
            print(f"def {func_name}({args_str}) -> {res_str}:")

        if restype in structs:
            print(f"    return c_{func_name}({c_params_str}).py")
        else:
            print(f"    return c_{func_name}({c_params_str})")


if __name__ == "__main__":
    generate_bindings()
