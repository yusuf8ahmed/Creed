try: 
    # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: 
    # for pip <= 9.0.3
    from pip.req import parse_requirements

from operator import attrgetter
from os import path
from setuptools import setup, find_packages

def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()

def from_here(relative_path):
    return path.join(path.dirname(__file__), relative_path)


# python -m twine upload dist/*

# env\Scripts\activate
# python setup.py sdist bdist_wheel
# python -m twine upload --skip-existing dist/*

# env\Scripts\activate && python setup.py sdist bdist_wheel && python -m twine upload --skip-existing dist/*
# python setup.py sdist bdist_wheel && python -m twine upload --skip-existing dist/*

setup(
    name="creed",
    version="0.2.3",
    install_requires=[
        "pypiwin32==223",
        "win10toast==0.9"
    ],
    author="Yusuf Ahmed",
    author_email="yusufahmed172@gmail.com",
    description="the one and only cross-platform Toaster/Notification in python",
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    url="https://github.com/yusuf8ahmed/Creed",
    packages=find_packages(),
        package_data={
        '': ['*.txt'],
        'creed': ['*.ico'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)