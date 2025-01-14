from setuptools import setup, find_packages

setup(
    name="LogFusion",
    version="0.1.1",
    description="A tool for running shell commands with animated output.",
    author="ILKAY-BRAHIM",
    author_email="ibrahimchifour@gmail.com",
    url="https://github.com/ILKAY-BRAHIM/LogFusion",
    packages=find_packages(),
    install_requires=[
        "colorama>=0.4.6",
    ],
    entry_points={
        "console_scripts": [
            "LogFusion=LogFusion.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
