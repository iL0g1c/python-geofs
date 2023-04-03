from setuptools import setup, find_namespace_packages

classifiers = [
"Development Status :: 3 - Alpha",
"Intended Audience :: Developers",
"Operating System :: Microsoft :: Windows : Windows 10",
"License :: OSI Approved :: MIT License",
"Programming Language :: Python :: 3",
]

setup(
    name="python-geofs",
    version="0.1.4b1",
    description="An abstraction layer for the GeoFS API",
    url="https://github.com/iL0g1c/python-geofs",
    long_description="Documentation for this script is on github at: https://github.com/iL0g1c/python-geofs",
    author="Osprey",
    install_requires=[],
    license="MIT",
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    package_data={
        "geofs.data": ["*.json"],
    }
)