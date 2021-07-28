from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='mylibrary',
    version='0.1',
    py_modules=['cli'],
    author = 'Kushal Kumar',
    author_email = 'kushalkumargupta4@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license = 'Apache 2.0',
    description = 'Converts Python API to Server',
    install_requires=['autopep8'],
    entry_points='''
        [console_scripts]
        mylibrary=cli:cli
    ''',
)
