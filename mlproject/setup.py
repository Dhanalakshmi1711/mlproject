from setuptools import find_packages, setup
from typing import List


def get_requirement(file_path: str) -> List[str]:
    '''
    this function will return a list of requirements
    :param file_path:
    :return:
    '''
    requirement = []
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace("\n", " ") for req in requirement]
        if "-e." in requirement:
            requirement.remove("-e.")

    return requirement


setup(
    name="mlproject0",
    version="0.0.1",
    author="dhana",
    authod_email="dhanalakshmisudarsanan@gmail.com",
    packages=find_packages(),
    install_requires=get_requirement("requirement.txt")

)
