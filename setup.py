from setuptools import find_packages, setup
from typing import List

HYPEN_R_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_R_DOT in requirements:
            requirements.remove(HYPEN_R_DOT)

    return requirements

setup(
    name='Industrial-Copper-Modeling',
    version='0.0.1',
    author='Mukesh Sharma',
    author_email='mukesh10400@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
