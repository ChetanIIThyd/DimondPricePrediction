from setuptools import find_packages ,setup
from typing import List

import os

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = [line.strip() for line in file_obj]
        
    requirements = [req for req in requirements if req != HYPHEN_E_DOT]
    
    return requirements



setup(
    name = 'DiamondPricePredication',
    version = '0.0.1' , 
    author = 'Chetan' ,
    author_email='chetan0gowda@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)