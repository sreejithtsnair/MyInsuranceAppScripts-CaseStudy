
from setuptools import setup, find_packages

setup(
    name='myinsuranceappscripts',
    version='0.12',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package',
    long_description=open('README.txt').read(),
    install_requires=['numpy'],
    url='https://github.com/sreejithtsnair/MyInsuranceAppScripts-CaseStudy.git',
    author='SreeRincyUnax',
    author_email='team1@example.com'
)
