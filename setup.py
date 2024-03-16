from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Simulated Annealing',
    ext_modules=cythonize("simulated_annealing.pyx"),
)