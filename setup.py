import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="humpday",
    version="0.6.2",
    description="Taking the pain out of choosing a Python global optimizer",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/microprediction/humpday",
    author="microprediction",
    author_email="pcotton@intechinvestments.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["humpday", "humpday.objectives", "humpday.optimizers", "humpday.comparison", "humpday.visualization","humpday.transforms"],
    test_suite='pytest',
    tests_require=['pytest'],
    include_package_data=True,
    install_requires=["wheel", "pathlib", "numpy>=1.19.5", "importlib-metadata>=1.7.0", "getjson",
                      "scipy", "funcy", "scipy","winning>=0.2.0",
                       "landscapes",  "pymorton","nevergrad","optuna"],
    entry_points={
        "console_scripts": [
            "humpday=humpday.__main__:main",
        ]
    },
)
