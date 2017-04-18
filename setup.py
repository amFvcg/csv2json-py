from setuptools import setup, find_packages


setup(
    name='csv2json',
    version='0.1.0',
    author='amFvcg',
    description='not-so-simple converter from csv to JSON',
#    long_description=read('README.md'),
    packages=['csv2json'],
    entry_points={
        'console_scripts': [
            'csv2json = csv2json.__main__:main'
        ]
    },
    test_suite='tests'
)
