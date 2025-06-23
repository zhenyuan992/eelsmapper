from setuptools import setup, find_packages

setup(
    name='eelsmapper',
    version='0.1.0',
    description='Data-driven analysis pipeline for STEM-EELS spectra',
    author='Yeo Zhen Yuan',
    author_email='yeozy@nus.edu.sg',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scikit-learn',
        'matplotlib'
    ],
    python_requires='>=3.8',
)
