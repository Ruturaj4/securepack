from setuptools import setup
setup(
    name='securepack',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'securepack=securepack:securepack'
        ]
    }
)