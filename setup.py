from setuptools import setup, find_packages

setup(
    name="IRStockData",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # list of dependencies
    ],
    author="Amin Najafgholizadeh",
    author_email="najafgholizadehamin@gmail.com",
    description="A Python package to download time candles and tick data of Iran stock market symbols",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AminWork/IRStockData",
)
