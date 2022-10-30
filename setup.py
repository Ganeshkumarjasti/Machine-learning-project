
from setuptools import setup
from typing import List




#Declaring Variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Ganesh Kumar"
DESCRIPTION="This is the first FSDS nov batch Machine Learning Project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description:This function is going to return list of requirement
    mention in requirements.txt

    return This function is going to return a list which contain name of libraries mentioned in requirements.txt file

    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readline()
        



setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()
)

