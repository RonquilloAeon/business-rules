from setuptools import setup, find_packages

from business_rules import __version__ as version

with open("HISTORY.rst") as f:
    history = f.read()

description = (
    "Python DSL for setting up business intelligence rules that can be "
    "configured without code"
)

setup(
    name="business-rules-reloaded",
    version=version,
    description="{0}\n\n{1}".format(description, history),
    author="RonquilloAeon",
    author_email="23411718+RonquilloAeon@users.noreply.github.com",
    url="https://github.com/RonquilloAeon/business-rules",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.7,<4",
)
