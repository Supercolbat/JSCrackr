from setuptools import setup
from typing import List
import jscrackr

def long_description() -> str:
    with open("README.md", encoding="utf-8") as file:
        return file.read()

def install_requires() -> List[str]:
    with open("requirements.txt", encoding="utf-8") as file:
        return file.read().strip().splitlines()

setup(
    name="JSCrackr",
    version=jscrackr.__version__,
    description=jscrackr.__doc__.strip(),
    long_description=long_description(),
    long_description_content_type="text/markdown",

    author=jscrackr.__author__,
    author_email="supercolbat@gmail.com",

    license=jscrackr.__license__,
    keywords=["deobfuscator"],
    python_requires=">=3.6",
    
    download_url="https://github.com/Supercolbat/.../",
    install_requires=install_requires(),
    
    entry_points={"console_scripts": ["jscrackr = jscrackr.__main__:main"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Terminals",
        "Topic :: Text Processing",
        "Topic :: Utilities"
    ],
    project_urls={
        "GitHub": "https://github.com/Supercolbat/..."
    },
)