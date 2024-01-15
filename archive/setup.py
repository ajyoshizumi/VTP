from setuptools import setup, find_packages

setup(
    name='vtp',
    version='1.0.0',
    author='Alexander Yoshizumi',
    author_email='ajy@applieddataresearch.org',
    description='VTP is a Python package that contains functions for processing vehicle telematics data and characterizing the driving activity of a vehicle.',
    url='git@github.com:ajyoshizumi/VTP.git',
    license='Apache-2.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache License 2.0',
        'Operating System :: OS Independent',
    ],
    package_dir={'':'src'},
    packages = find_packages(where="src"),
    python_requires='>=3.7',
    zip_safe=False
)