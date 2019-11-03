import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="math-expression-parser-ALIEZZAT", # Replace with your own username
    version="0.0.1",
    author="ALIEZZAT ODEH",
    author_email="aliezzat1993@outlook.com",
    description="A package for parsing mathmatical expressions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)