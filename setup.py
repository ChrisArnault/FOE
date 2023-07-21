import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE/"README.md").read_text()
VERSION = (HERE/"VERSION").read_text()

setup(
    name = "FOE",
    version = VERSION,
    description = "Outil de modélisation pour Forge of Empire",
    long_description = README,
    long_description_content_type = "text/markdown",
    url = "https://github.com/ChrisArnault/FOE#readme",
    author = "Chris Arnault",
    author_email = "chris.arnault@gmail.com",
    license = "CeCILL-B",
    classifiers = [
        "License :: CeCILL-B Free Software License Agreement (CECILL-B)",
        "Programming Language :: Python :: 3",
    ],
    packages = ["FOE"],
    include_package_data = True,

    package_data = {},

    install_requires = [
    ],

    entry_points = {
        "console_scripts": [
            "FOE = FOE:__main__.main",
        ]
    },
)
