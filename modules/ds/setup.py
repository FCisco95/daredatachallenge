from setuptools import setup

setup(
    name='model',
    version='0.1.0',
    description='A machine learning model for predicting padel players ranking points',
    url='https://github.com/FCisco95/daredatachallenge',
    author='Joao Francisco Vieira',
    author_email='joao_vieira25@hotmail.com',
    packages=['model'],
    install_requires=['pandas', 'scikit-learn'],
)
