from setuptools import find_packages, setup

setup(
    name='mylibrary',
    paccages=find_packages(include='mylibrary'),
    version='0.0.1',
    description = 'My Python Library',
    author="Me",
    license="MIT",
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_requires=['python==4.4.1'],
    test_suite='tests',
)
