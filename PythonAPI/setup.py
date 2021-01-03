#!/usr/bin/env python
# To compile and install locally run:
#   $ python setup.py build_ext --inplace
# To install library to Python site-packages run:
#   $ python setup.py build_ext install

from setuptools import Extension, setup


try:
    from Cython.Build import cythonize
    import numpy as np

    ext_modules = cythonize(
        [
            Extension(
                'pycocotools._mask',
                sources=['../common/maskApi.c', 'pycocotools/_mask.pyx'],
                include_dirs=[np.get_include(), '../common'],
                extra_compile_args=[
                    '-Wno-cpp', '-Wno-unused-function', '-std=c99'
                ],
            ),
        ],
        compiler_directives={'language_level': '3'},
    )
except ImportError:
    ext_modules = None


setup(
    name='pycocotools',
    version='2.0.2',
    packages=['pycocotools'],
    package_dir={'pycocotools': 'pycocotools'},
    install_requires=[
        'numpy>=1.16.4',
        'cython>=0.27.3',
    ],
    extras_require={
        'viz': ['matplotlib>=2.1.0'],
    },
    ext_modules=ext_modules,
)
