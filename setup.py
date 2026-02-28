from setuptools import find_packages, setup

setup(
    name='deepmd_jax',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'jax[cuda12]>=0.7.1',
        'flax',
        'optax',
        'jax-md>=0.2.27',
        'ase',
        'matplotlib',
        'gpustat',
        'ipykernel',
    ],
    author='Ruiqi Gao',
    author_email='ruiqigao@princeton.edu',
    description='DP-JAX',
    url='https://github.com/SparkyTruck/deepmd-jax',
    python_requires='>=3.10',
)
