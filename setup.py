from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = "-e ."
def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the requiremnts
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements= [req.replace("/n","") for req in requirements if req != HYPHEN_E_DOT]
    return requirements

setup(
    name = "END_to_END_ML",
    version = "0.0.1",
    author = "shadman",
    author_email = "shadmanqaisar7@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)