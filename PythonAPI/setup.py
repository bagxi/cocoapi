from setuptools import Extension, setup

import numpy as np

# To compile and install locally run "python setup.py build_ext --inplace"
# To install library to Python site-packages run "python setup.py build_ext install"

ext_modules = [
    Extension(
        'pycocotools._mask',
        sources=['../common/maskApi.c', 'pycocotools/_mask.pyx'],
        include_dirs=[np.get_include(), '../common'],
        extra_compile_args=['-Wno-cpp', '-Wno-unused-function', '-std=c99'],
    )
]

setup(
    name='pycocotools',
    version='2.0.1',
    packages=['pycocotools'],
    package_dir={'pycocotools': 'pycocotools'},
    install_requires=[
        'setuptools>=18.0',
        'numpy>=1.16.4',
        'cython>=0.27.3',
    ],
    extras_require={
        'viz':  ['matplotlib>=2.1.0'],
    },
    ext_modules=ext_modules
)
