import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='securepack',
    version='0.0.5',
    author="Ruturaj Kiran Vaidya",
    author_email="ruturajkvaidya@gmail.com",
    description="Securepack helps securing packages from typosquatting attack",
    long_description_content_type="text/markdown",
    url="https://github.com/Ruturaj4/securepack",
    packages=setuptools.find_packages(),
    long_description=long_description,
    entry_points={
        'console_scripts': [
            'securepack=securepack.__main__:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
       'fuzzyset',
       'python-levenshtein',
       'texttable'
    ]
)
