from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="alasan",
    version="0.0.1",
    author="Lucas Hild",
    author_email="contact@lucas-hild.de",
    description="Alasan helps you build Alexa skills on AWS Lambda using Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Lanseuo/alasan",
    packages=find_packages()
)
