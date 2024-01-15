from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='vtp',
    version='1.0.0',
    description='Package contains functions for processing vehicle telematics data and characterizing the driving activity of a vehicle.',
    package_dir={'': 'vtp'},
    packages=find_packages(where='vtp'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ajyoshizumi/vtp',
    author='Alexander Yoshizumi',
    author_email='alexanderyoshizumi@applieddataresearch.org',
    license='Apache-2.0',
    classifiers=[
        'License :: OSI Approved :: Apache License 2.0',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    install_requires=['glob2 >= 0.7',
                      'numpy >= 1.26.3',
                      'pandas >= 2.1.4'
                      ],
    python_requires=">=3.10",
)