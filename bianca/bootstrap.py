import asyncio
import ctypes
import datetime
import json
import logging
import os
import sys
import time
import uuid

from contextlib import asynccontextmanager
from logging import LogRecord
from pathlib import Path
from typing import Generator
from tempfile import TemporaryDirectory

__all__ = [
    "asyncio",
    "ctypes",
    "datetime",
    "json",
    "logging",
    "os",
    "sys",
    "time",
    "uuid",

    "PROJECT_DIR",
    "LLAMA_DIR",
    "LLAMA_VERSION",
    "LLAMA_LIB_DIR",
    "LLAMA_LIB",
    "common_exec",

    "asynccontextmanager",
    "LogRecord",
    "Path",
    "Generator"
]

PROJECT_DIR = Path.home() / ".local" / "share" / "bianca"
PROJECT_DIR.mkdir(parents=True, exist_ok=True)

LLAMA_DIR = PROJECT_DIR / "llama"
LLAMA_VERSION = LLAMA_DIR / ".version"
LLAMA_LIB_DIR = LLAMA_DIR / "lib"
LLAMA_LIB = LLAMA_LIB_DIR / "libllama.so"


async def common_exec(program: str, *args: str, **kwargs) -> str:
    process = await asyncio.create_subprocess_exec(
        program, *args, **kwargs,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()
    if process.returncode != 0:
        stderr = stderr.decode().strip()
        raise RuntimeError(f"{program} failed with exit code {process.returncode}\n{stderr}")
    return stdout.decode().strip()


async def _setup_llama():
    async def _get_upstream_version() -> str:
        import httpx
        url = "https://github.com/ggml-org/llama.cpp/releases/latest"
        async with httpx.AsyncClient() as client:
            for _ in range(3):
                response = await client.head(url)
                if response.status_code in range(300, 400):
                    return response.headers["location"].split("/")[-1]
            raise RuntimeError(f"failed to request latest llama.cpp release (status code: {response.status_code})")

    async def _get_local_version() -> str:
        if LLAMA_VERSION.is_file():
            return LLAMA_VERSION.read_text().strip()
        return "-1"

    upstream_version, local_version = await asyncio.gather(
        _get_upstream_version(),
        _get_local_version())

    if upstream_version == local_version:
        return

    hip_config_l, hip_config_r = await asyncio.gather(
        common_exec("hipconfig", "-l", cwd=str(PROJECT_DIR)),
        common_exec("hipconfig", "-R", cwd=str(PROJECT_DIR)))

    env = os.environ.copy()
    env["HIP_FORCE_DEV_KERNARG"] = "1"
    env["ROCM_VISIBLE_DEVICES"] = "0"
    env["AMD_LOG_LEVEL"] = "0"
    env["HSA_ENABLE_SDMA"] = "0"
    env["HIPCXX"] = f"{hip_config_l}/clang"
    env["HIP_PATH"] = hip_config_r

    host_release_flags = " ".join((
        "-O3", "-DNDEBUG", "-pipe",
        "-march=native", "-mtune=native",
        "-fno-plt", "-fno-semantic-interposition",
        "-fno-math-errno", "-fno-trapping-math",
        "-funroll-loops", "-fomit-frame-pointer",
    ))
    hip_release_flags = " ".join((
        "-O3", "-DNDEBUG",
        "-fno-math-errno", "-fno-trapping-math",
        "-ffp-contract=fast",
        "-munsafe-fp-atomics",
    ))
    link_release_flags = "-Wl,-O1 -Wl,--as-needed -Wl,--gc-sections"

    cpu_count = os.cpu_count() or 8

    with TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        build_dir = temp_path / "build"

        await common_exec(
            "git", "clone",
            "--depth", "1",
            "--branch", upstream_version,
            "https://github.com/ggml-org/llama.cpp.git", ".",
            env=env, cwd=str(temp_dir))

        await common_exec(
            "cmake",
            "-B", str(build_dir),
            "-S", str(temp_path),
            "-G", "Ninja",

            "-DCMAKE_BUILD_TYPE=Release",
            "-DCMAKE_INTERPROCEDURAL_OPTIMIZATION=ON",
            "-DCMAKE_POSITION_INDEPENDENT_CODE=ON",
            f"-DCMAKE_C_FLAGS_RELEASE={host_release_flags}",
            f"-DCMAKE_CXX_FLAGS_RELEASE={host_release_flags}",
            f"-DCMAKE_HIP_FLAGS_RELEASE={hip_release_flags}",
            f"-DCMAKE_EXE_LINKER_FLAGS_RELEASE={link_release_flags}",
            f"-DCMAKE_SHARED_LINKER_FLAGS_RELEASE={link_release_flags}",
            f"-DCMAKE_MODULE_LINKER_FLAGS_RELEASE={link_release_flags}",

            "-DBUILD_SHARED_LIBS=ON",
            "-DLLAMA_BUILD_COMMON=OFF",
            "-DLLAMA_BUILD_TESTS=OFF",
            "-DLLAMA_BUILD_TOOLS=OFF",
            "-DLLAMA_BUILD_EXAMPLES=OFF",
            "-DLLAMA_BUILD_SERVER=OFF",
            "-DLLAMA_BUILD_APP=OFF",
            "-DLLAMA_OPENSSL=OFF",
            "-DGGML_BUILD_TESTS=OFF",
            "-DGGML_BUILD_EXAMPLES=OFF",

            "-DGGML_NATIVE=ON",
            "-DGGML_LTO=ON",
            "-DGGML_CCACHE=ON",
            "-DGGML_OPENMP=ON",
            "-DGGML_BACKEND_DL=OFF",

            "-DGGML_HIP=ON",
            "-DGGML_HIPBLAS=ON",
            "-DGGML_HIP_GRAPHS=ON",
            "-DGGML_HIP_NO_VMM=ON",
            "-DGGML_HIP_MMQ_MFMA=ON",
            "-DGGML_HIP_ROCWMMA_FATTN=ON",
            "-DGGML_CUDA_FA=ON",
            "-DGGML_CUDA_FA_ALL_QUANTS=ON",
            "-DGGML_CUDA_FORCE_MMQ=ON",
            "-DGGML_CUDA_GRAPHS=ON",
            "-DGGML_KQUANTS_ROW_MAJOR=ON",
            "-DGPU_TARGETS=gfx1100",
            "-DAMDGPU_TARGETS=gfx1100",
            "-DCMAKE_HIP_ARCHITECTURES=gfx1100",

            "-DGGML_CUDA=OFF",
            "-DGGML_VULKAN=OFF",
            "-DGGML_SYCL=OFF",
            "-DGGML_METAL=OFF",
            "-DGGML_OPENCL=OFF",
            "-DGGML_RPC=OFF",
            "-DGGML_BLAS=OFF",

            f"-DCMAKE_INSTALL_PREFIX={LLAMA_DIR}",
            env=env, cwd=str(temp_dir))

        await common_exec(
            "cmake", "--build", ".", "--config", "Release",
            "--parallel", str(cpu_count),
            env=env, cwd=str(build_dir))

        await common_exec(
            "cmake", "--install", ".", "--strip",
            env=env, cwd=str(build_dir))

    LLAMA_VERSION.write_text(upstream_version)


def bootstrap():
    os.chdir(str(PROJECT_DIR))
    asyncio.run(_setup_llama())


bootstrap()
