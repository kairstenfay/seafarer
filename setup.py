import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="seafarer",
    version="0.0.1",
    author="Kairsten Fay",
    author_email="kairstenfay@gmail.com",
    description="An additional layer of abstraction for seaborn and matplotlib plots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kairstenfay/seafarer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)