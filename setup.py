
from setuptools import setup, find_packages

setup(
    name='myinsurancescripts',
    version='0.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package',
    long_description=open('README.txt').read(),
    install_requires=['numpy'],
    url='https://github.com/sreejithtsnair/MyInsuranceAppScripts-CaseStudy.git',
    author='Rincy_Unax_Sree',
    author_email='team1@example.com'
)
