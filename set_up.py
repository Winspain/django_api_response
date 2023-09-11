from setuptools import setup, find_packages

from django_useful_utils.api_logging_middleware import VERSION

setup(
    name='django_useful_utils',
    version=VERSION,
    python_requires='>=3.8',
    packages=find_packages(),
    install_requires=[],
    description='',
    author='winspain',
    author_email='',
    classifiers=[
        'License :: Apache License Version 2.0',

        'Operating System :: POSIX :: Linux',

        'Programming Language :: Python :: 3.11',
    ],
)
