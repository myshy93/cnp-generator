import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='cnp-generator',
    version='1.1.1',
    url='https://github.com/myshy93/cnp-generator',
    author='Mihai Dinu',
    author_email='mihai.dinu93@gmail.com',
    license='MIT',
    keywords='cnp romania generator decoder',
    description='Romania CNP number generator and decoder.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['cnpgen'],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
