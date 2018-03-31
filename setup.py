from setuptools import setup
from setuptools.extension import Extension
from Cython.Distutils import build_ext
from os.path import join
import functools

import os

rel = functools.partial(join, os.getcwd())

ext_modules = [
    Extension(
        "_pybloof",
        extra_compile_args=['-std=gnu99', '-O2', '-D_LARGEFILE64_SOURCE'],
        sources=["src/_pybloof.pyx",
                 'src/MurmurHash3.c'],

        include_dirs=[rel('src')],
        library_dirs=[rel('src')]
    )
]

setup(
    name='pybloof',
    version='0.7.3',
    author='Jake Heinz',
    author_email='me@jh.gg',
    url="http://github.com/jhgg/pybloof",
    description='A high performance python bloom filter thing.',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
    ],
    license='MIT License',
    cmdclass={'build_ext': build_ext},
    zip_safe=False,
    package_dir={'': 'src'},
    py_modules=['pybloof'],
    ext_modules=ext_modules,
    test_suite='nose.collector',
    install_requires=[
        'Cython',
        'bitarray'
    ]
)
