![autoray-header](https://github.com/jcmgray/autoray/assets/8982598/c5cb89bf-cc16-4345-8796-e0bd98dc2a15)

[![tests](https://github.com/jcmgray/autoray/actions/workflows/tests.yml/badge.svg)](https://github.com/jcmgray/autoray/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/jcmgray/autoray/branch/main/graph/badge.svg?token=Q5evNiuT9S)](https://codecov.io/gh/jcmgray/autoray)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/ba896d74c4954dd58da01df30c7bf326)](https://app.codacy.com/gh/jcmgray/autoray/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![Docs](https://readthedocs.org/projects/autoray/badge/?version=latest)](https://autoray.readthedocs.io)
[![PyPI](https://img.shields.io/pypi/v/autoray?color=teal)](https://pypi.org/project/autoray/)
[![Anaconda-Server Badge](https://anaconda.org/conda-forge/autoray/badges/version.svg)](https://anaconda.org/conda-forge/autoray)

[`autoray`](https://autoray.readthedocs.io/en/latest) is a lightweight python AUTOmatic-arRAY library for
abstracting your tensor operations. Primarily it provides an
[*automatic* dispatch mechanism](https://autoray.readthedocs.io/en/latest/automatic_dispatch.html#)
that means you can write backend agnostic code that works for:

* [numpy](https://github.com/numpy/numpy)
* [pytorch](https://pytorch.org/)
* [jax](https://github.com/google/jax)
* [cupy](https://github.com/cupy/cupy)
* [dask](https://github.com/dask/dask)
* [autograd](https://github.com/HIPS/autograd)
* [tensorflow](https://github.com/tensorflow/tensorflow)
* [sparse](https://sparse.pydata.org/)
* [mars](https://github.com/mars-project/mars)
* ... and indeed **any** library that provides a numpy-*ish* api, even if it
  knows nothing about `autoray`.

Beyond that, abstracting the array interface allows you to:

* *swap [custom versions of functions](https://autoray.readthedocs.io/en/latest/automatic_dispatch.html#functions)
  for specific backends*
* *trace through computations [lazily](https://autoray.readthedocs.io/en/latest/lazy_computation.html) without actually
  running them*
* *automatically [share intermediates and fold constants](https://autoray.readthedocs.io/en/latest/lazy_computation.html#sharing-intermediates)
  in computations*
* *compile functions with a [unified interface](https://autoray.readthedocs.io/en/latest/compilation.html) for different
  backends*


## Basic usage

The main function of `autoray` is
[`do`](https://autoray.readthedocs.io/en/latest/autoapi/autoray/autoray/index.html#autoray.autoray.do),
which takes a function
name followed by `*args` and `**kwargs`, and automatically looks up (and
caches) the correct function to match the equivalent numpy call:

```python
from autoray as ar

def noised_svd(x):
    # automatic dispatch based on supplied array
    U, s, VH = ar.do('linalg.svd', x)

    # automatic dispatch based on different array
    sn = s + 0.1 * ar.do('random.normal', size=ar.shape(s), like=s)

    # automatic dispatch for multiple arrays for certain functions
    return ar.do('einsum', 'ij,j,jk->ik', U, sn, VH)

# explicit backend given by string
x = ar.do('random.uniform', size=(100, 100), like="torch")

# this function now works for any backend
y = noised_svd(x)

# explicit inference of backend from array
ar.infer_backend(y)
# 'torch'
```

If you don't like the explicit `do` syntax, or simply want a
drop-in replacement for existing code, you can also import the `autoray.numpy`
module:

```python
from autoray import numpy as np

# set a temporary default backend
with ar.backend_like('cupy'):
    z = np.ones((3, 4), dtype='float32')

np.exp(z)
# array([[2.7182817, 2.7182817, 2.7182817, 2.7182817],
#        [2.7182817, 2.7182817, 2.7182817, 2.7182817],
#        [2.7182817, 2.7182817, 2.7182817, 2.7182817]], dtype=float32)
```

Custom backends and functions can be dynamically registered with:

* [`register_backend`](https://autoray.readthedocs.io/en/latest/autoapi/autoray/autoray/index.html#autoray.autoray.register_backend)
* [`register_function`](https://autoray.readthedocs.io/en/latest/autoapi/autoray/autoray/index.html#autoray.autoray.register_function)

The main documentation is available at [autoray.readthedocs.io](https://autoray.readthedocs.io/en/latest/).
