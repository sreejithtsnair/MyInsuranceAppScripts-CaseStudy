
from setuptools import setup, find_packages

setup(
<<<<<<< HEAD
    name='myinsurancescripts',
    version='0.4',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package - updated',
=======
    name='myinsuranceappscripts',
    version='0.12',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package',
    long_description=open('README.txt').read(),
>>>>>>> cff6fec81da4329b2b6bb6caa96e423d2e2ad504
    install_requires=['numpy'],
    url='https://github.com/sreejithtsnair/MyInsuranceAppScripts-CaseStudy.git',
    author='SreeRincyUnax',
    author_email='team1@example.com'
)
