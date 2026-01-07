from setuptools import setup, find_packages

setup(
    name="coordinate-converter",
    version="1.0.0",
    description="WGS84 ↔ ITM coordinate conversion tool",
    author="Arife Mutlu",
    author_email="arife.mutlu@outlook.com",
    url="https://github.com/ArifeMutlu/coordinate-converter",
    packages=find_packages(),
    install_requires=[
        "pyproj>=3.6.1",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
