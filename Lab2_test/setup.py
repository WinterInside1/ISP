from setuptools import setup, find_packages

setup(
    name='CustomSerializer',
    python_requires='>3.8',
    version='0.2',
    packages=find_packages(),
    description='Lab2_final_test',
    install_requires=['toml', 'PyYAML'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest-cov'],
    test_suite='tests',
    scripts=['script/entrypoint']
)
