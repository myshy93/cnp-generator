# CNP generator and decoder

##  📖 About
Cnp-generator package contains both a Python lib and CLI tool for generate and decode CNPs.

With CLI tool you can:
- generate a valid CNP based on gender, region, and birth date.
- check if a CNP is valid
- decode CNP information
- generate random CNPs for testing purposes

Python lib contains `Cnp` class that will provide all functionalities available in tool to be used in code.

## 💻 Tool Usage
Run CNP tool with:

`python -m cnpgen
`

Available options:

    -h --help   Show help.
    --version   Show program version.
    -c          Start new CNP wizard. Guided wizard for genereating a CNP based on input info.
    -g N        Generate N random CNPs.
    -i CNP      Show relevant information about CNP. 

## 🧪 API Usage

### Quick start
```python
from datetime import date
from cnpgen import Cnp, Gender, Region
print(Cnp(Gender.F, date(1993, 3, 4), Region.Bucuresti))

>>> 2930304400014
```

### Full documentation

Soon available on Readthedocs.