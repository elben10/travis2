from setuptools import find_packages, setup

docs_requirements = []

installation_requirements = []

setup_requirements = [
    "pytest-runner"
]

test_requirements = [
    "pytest",
    "cerberus",
]

setup(
    name='MyPackageName',
    version='1.0.0',
    url='https://github.com/mypackage.git',
    author='Author Name',
    author_email='author@gmail.com',
    description='Description of my package',
    packages=find_packages(),    
    install_requires=installation_requirements,
    setup_requires=setup_requirements,
    extras_require={
        'docs': docs_requirements,
        'test': test_requirements,
    }
)
