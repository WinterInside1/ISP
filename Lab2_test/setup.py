from setuptools import setup, find_packages

setup(
    name='CustomSerializer',
    python_requires='>3.8',
    version='0.2',
    packages=find_packages(),
    description='Lab2_test',
    install_requires=['toml', 'PyYAML', 'json', 'pickle'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
    scripts=['script/entrypoint']
)
