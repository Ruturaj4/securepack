from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='securepack',
    version='0.0.1',
    author="Ruturaj Kiran Vaidya",
    author_email="ruturajkvaidya@gmail.com",
    description="Securepack helps securing packages from typosquatting attack
",
    long_description_content_type="text/markdown",
    url="https://github.com/Ruturaj4/securepack",
    packages=setuptools.find_packages(),
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
       'fuzzyset>=0.0.18',
    ]
)
