from setuptools import setup, find_packages
from pathlib import Path

# Read long description from README.md
this_dir = Path(__file__).parent
long_description = (this_dir / "README.md").read_text(encoding="utf-8")

setup(
    name='eelsmapper',
    version='0.1.2',
    description='Data-driven analysis pipeline for STEM-EELS spectra',
    author='Yeo Zhen Yuan',
    author_email='yeozy@nus.edu.sg',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'numpy',
        'scikit-learn',
        'matplotlib'
    ],
    python_requires='>=3.8',
)
