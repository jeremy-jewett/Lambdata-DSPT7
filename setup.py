<<<<<<< HEAD
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata_mod", # the name that you will install via pip
    version="1.0",
    author="Jeremy Jewett",
    author_email="jeremy.jewett@gmail.com",
    description="multiplies a number by 100",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/YOUR_USERNAME/YOUR_REPO_NAME",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
=======
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata_mod", # the name that you will install via pip
    version="1.0",
    author="Jeremy Jewett",
    author_email="jeremy.jewett@gmail.com",
    description="multiplies a number by 100",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/YOUR_USERNAME/YOUR_REPO_NAME",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
>>>>>>> f2d7572b1ad105a5c13b6847186fa150cfa8f865
)