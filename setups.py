from setuptools import find_packages,setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "End-to-End-ML-Project"
AUTHOR_USER_NAME = "parthalathiya034"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "lathiyap46@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    # packages = find_packages(),
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },


    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
  

