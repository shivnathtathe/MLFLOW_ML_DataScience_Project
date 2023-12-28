import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "MLFLOW_ML_DataScience_Project"
AUTHOR_USER_NAME = "ShivnathTathe"
SRC_REPO = "DataScienceProject"
AUTHOR_EMAIL = "sptathe2001@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/shivnathtathe/MLFLOW_ML_DataScience_Project",
    project_urls={
        "Bug Tracker": f"https://github.com/shivnathtathe/MLFLOW_ML_DataScience_Project",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)