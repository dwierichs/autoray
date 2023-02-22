try:
    # -- Distribution mode --
    # import from _version.py generated by setuptools_scm during release
    from ._version import version as __version__
except ImportError:
    # -- Source mode --
    try:
        # use setuptools_scm to get the current version from src using git
        from setuptools_scm import get_version as _gv
        from pathlib import Path as _Path
        __version__ = _gv(_Path(__file__).parent.parent)
    except ImportError:
        # setuptools_scm is not available, use a default version
        __version__ = "0.0.0+unknown"


from .autoray import (
    do,
    get_backend,
    set_backend,
    backend_like,
    infer_backend,
    infer_backend_multi,
    get_lib_fn,
    shape,
    ndim,
    conj,
    transpose,
    dag,
    real,
    imag,
    reshape,
    to_backend_dtype,
    astype,
    get_dtype_name,
    get_common_dtype,
    to_numpy,
    register_backend,
    register_function,
    # tree utilities
    is_array,
    tree_map,
    tree_iter,
    tree_apply,
    tree_flatten,
    tree_unflatten,
    compose,
    # the numpy mimic submodule
    numpy,
)
from .compiler import autojit
from . import lazy


__all__ = (
    "do",
    "get_backend",
    "set_backend",
    "backend_like",
    "infer_backend",
    "infer_backend_multi",
    "get_lib_fn",
    "shape",
    "ndim",
    "conj",
    "transpose",
    "dag",
    "real",
    "imag",
    "reshape",
    "to_backend_dtype",
    "get_dtype_name",
    "get_common_dtype",
    "astype",
    "to_numpy",
    "register_backend",
    "register_function",
    # tree utilities
    "is_array",
    "tree_map",
    "tree_iter",
    "tree_apply",
    "tree_flatten",
    "tree_unflatten",
    "compose",
    # the numpy mimic submodule
    "numpy",
    # abstract function compilation
    "autojit",
    # lazy array library
    "lazy",
)
