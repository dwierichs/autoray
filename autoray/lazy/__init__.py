from . import linalg

from .core import (
    LazyArray,
    Variable,
    shared_intermediates,
    array,
    transpose,
    reshape,
    tensordot,
    einsum,
    trace,
    matmul,
    kron,
    clip,
    flip,
    sort,
    argsort,
    stack,
    concatenate,
    split,
    # binary
    multiply,
    add,
    floordivide,
    truedivide,
    # unary
    sin,
    cos,
    tan,
    arcsin,
    arccos,
    arctan,
    sinh,
    cosh,
    tanh,
    arcsinh,
    arccosh,
    arctanh,
    sqrt,
    exp,
    log,
    log2,
    log10,
    conj,
    sign,
    angle,
    real,
    imag,
    # reductions
    prod,
)
from .core import abs_ as abs
from .core import sum_ as sum
from .core import min_ as min
from .core import max_ as max
from .core import complex_ as complex

__all__ = (
    "LazyArray",
    "Variable",
    "shared_intermediates",
    "linalg",
    "array",
    # basic and shape changing functions
    "transpose",
    "reshape",
    "tensordot",
    "einsum",
    "conj",
    "trace",
    "matmul",
    "kron",
    "clip",
    "flip",
    "sort",
    "argsort",
    "stack",
    "concatenate",
    "split",
    # binary functions
    "multiply",
    "add",
    "floordivide",
    "truedivide",
    # unary functions
    "sin",
    "cos",
    "tan",
    "arcsin",
    "arccos",
    "arctan",
    "sinh",
    "cosh",
    "tanh",
    "arcsinh",
    "arccosh",
    "arctanh",
    "sqrt",
    "exp",
    "log",
    "log2",
    "log10",
    "conj",
    "sign",
    "abs",
    "angle",
    "real",
    "imag",
    # reduction functions
    "sum",
    "prod",
    "min",
    "max",
    "complex",
)


try:
    from opt_einsum.backends.dispatch import _aliases

    _aliases["autoray"] = "autoray.lazy"
except ImportError:  # pragma: no cover
    pass
