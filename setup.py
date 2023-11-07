from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize("sqp/tools/cacher.pyx", annotate=True))
