from setuptools import setup, find_packages, __version__

setup(
    name='django_useful_utils',
    version='0.0.1',
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
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
)
