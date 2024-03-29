import setuptools

with open("README.MD","r", encoding="utf-8") as f:
    long_description=f.read()

__version__ = "0.0.0"

REPO_NAME="dvc_deeplearning_tensorflow_mlops"
AUTHOR_USER_NAME="VigneshwarKandhaiya1207"
AUTHOR_EMAIL="vigneshwar.k2@gmail.com"
SRC_REPO="dlproj"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="The Deeplearning Project with DVC setup",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    packages=["dlproj"]
)

