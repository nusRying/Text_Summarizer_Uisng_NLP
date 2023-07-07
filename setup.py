import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

__version__ = "0.0.1"

REPONAME = "text_Summarizer"
AUTHOR = "Umair"
SRC_REPO = "https://github.com/your-username/your-repo"
EMAIL = "umairejazbutt@gmail.com"
DESCRIPTION = "A template for creating a Python package for ML projects."

setuptools.setup(
    name=REPONAME,
    version=__version__,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=SRC_REPO,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
