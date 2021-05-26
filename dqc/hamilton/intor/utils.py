import os
import ctypes
import numpy as np
from typing import Dict, Any, Callable

# contains functions and constants that are used specifically for
# dqc.hamilton.intor files (no dependance on other files in dqc.hamilton.intor
# is required)

__all__ = ["NDIM", "CINT", "CGTO", "CPBC", "CSYMM", "c_null_ptr", "np2ctypes", "int2ctypes"]

# CONSTANTS
NDIM = 3

# libraries
_curpath = os.path.dirname(os.path.abspath(__file__))
_libcint_path = os.path.join(_curpath, "../../lib/libcint/build/libcint.so")
_libcgto_path = os.path.join(_curpath, "../../lib/libcgto.so")
_libcpbc_path = os.path.join(_curpath, "../../lib/libpbc.so")
# _libcvhf_path = os.path.join(_curpath, "../../lib/libcvhf.so")
_libcsymm_path = os.path.join(_curpath, "../../lib/libsymm.so")

_libs: Dict[str, Any] = {}

def _library_loader(name: str, path: str) -> Callable:
    # load the library and cache the handler
    def fcn():
        if name not in _libs:
            _libs[name] = ctypes.cdll.LoadLibrary(path)
        return _libs[name]
    return fcn

CINT = _library_loader("CINT", _libcint_path)
CGTO = _library_loader("CGTO", _libcgto_path)
CPBC = _library_loader("CPBC", _libcpbc_path)
# CVHF = _library_loader("CVHF", _libcvhf_path)
CSYMM = _library_loader("CSYMM", _libcsymm_path)

c_null_ptr = ctypes.POINTER(ctypes.c_void_p)

def np2ctypes(a: np.ndarray) -> ctypes.c_void_p:
    # get the ctypes of the numpy ndarray
    return a.ctypes.data_as(ctypes.c_void_p)

def int2ctypes(a: int) -> ctypes.c_int:
    # convert the python's integer to ctypes' integer
    return ctypes.c_int(a)
