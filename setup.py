from setuptools import find_packages
from setuptools import setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(path:str) -> List[str]:
    '''
    This function will return list of requirements
    '''



    with open(path) as f:
        req = [r.replace("\n","") for r in f.readlines()]
        if HYPEN_E_DOT in req:
            req.remove(HYPEN_E_DOT)
    return req

setup(
    name='Address Extractor',
    version='0.0.1',
    author='Ayman M. Ibrahim',
    author_email='ayman.ibrahim@theaddressholding.com',
    packages=find_packages(),
    install_requires=get_requirements('./requirments.txt')
)
