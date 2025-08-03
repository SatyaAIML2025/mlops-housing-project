from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MLOPS-ASSIGNMENT-1",
    version="1.0",
    author="A Satya - 2023AB05057",
    packages=find_packages(),
    install_requires = requirements,
)