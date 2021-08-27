"""
Robotframework-SauceLabs
"""
from pathlib import Path
from setuptools import setup

LIBRARY_NAME = "SauceLabs"
CWD = Path(__file__).parent

requirements_file = CWD / "requirements.txt"
readme_file = CWD / "README.md"

# Get requirements
with requirements_file.open(encoding="utf-8") as f:
    REQUIREMENTS = f.read().splitlines()

# Get the long description from the README file
with readme_file.open(encoding="utf-8") as f:
    long_description = f.read()

CLASSIFIERS = """
Development Status :: 3 - Alpha
Topic :: Software Development :: Testing
Operating System :: OS Independent
License :: OSI Approved :: Apache Software License
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Topic :: Software Development :: Testing
Framework :: Robot Framework
Framework :: Robot Framework :: Library
""".strip().splitlines()

setup(
    name="robotframework-{}".format(LIBRARY_NAME.lower()),
    version="0.1.0",
    description=" A Library for Working with Sauce Labs ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joshgrant/robotframework-saucelabs",
    author="Josh Grant",
    author_email="joshua.m.grant@gmail.com",
    license="MIT",
    classifiers=CLASSIFIERS,
    install_requires=REQUIREMENTS,
    keywords="robot framework testing automation selenium seleniumlibrary"
    "testability async javascript softwaretesting",
    platforms="any",
    packages=[LIBRARY_NAME],
    package_dir={"": "robotframework-saucelabs"},
)