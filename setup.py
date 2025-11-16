import subprocess
from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install

setup(
    name='deepmd_jax',
    packages=find_packages(),
    install_requires=[
        'jax[cuda12]==0.6.2',
        'flax==0.10.6',
        'optax==0.2.5',
        'jax-md @ git+https://github.com/google/jax-md.git',
        'ase',
        'matplotlib',
        'gpustat',
        'ipykernel',
        'seaborn',
        'pandas',
    ],
    description='DP-JAX',
    url='https://github.com/AMLS-PRG/deepmd-jax',
    python_requires='>=3.10',
)
