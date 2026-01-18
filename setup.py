from setuptools import find_packages, setup
from typing import List


HYPHEN_CONSTANT = '-e .'
def fetch_requirements(file_path: str)->List[str]:
    requirements=[]
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_CONSTANT in requirements:
            requirements.remove(HYPHEN_CONSTANT)

    return requirements


setup(
    name = 'revision-ml', 
    version = '0.0.1', 
    author = 'mili', 
    packages = find_packages(), 
    install_requires = fetch_requirements("requirements.txt")
)