from setuptools import find_packages, setup

requirements = [
    "numpy",
    "pandas",
]

setup(
    name = 'MyPackageName',
    version = '1.0.0',
    url = 'https://github.com/mypackage.git',
    author = 'Author Name',
    author_email = 'author@gmail.com',
    description = 'Description of my package',
    packages = find_packages(),    
    install_requires=requirements,
)
