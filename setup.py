import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flask-db",
    version="0.0.1",
    author="Jonatas Leon",
    author_email="me@jonatasleon.com",
    description="Flask application to show how use sqlalchemy_mixins.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonatasleon/flask-db",
    packages=setuptools.find_packages(),
)
