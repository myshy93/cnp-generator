"""CNP tool for handling CNP numbers."""

import argparse
import random
import sys
import time
from datetime import date

from .__init__ import Cnp, Gender, Region

VERSION = '1.1.1'
PROG_DESCRIPTION = "Cnpgen - CLI tool for handling CNP related tasks."
MIN_D_DATE_TS = time.mktime(time.strptime('1990-01-01', "%Y-%M-%d"))
MAX_D_DATE_TS = time.mktime(time.strptime('2099-12-31', "%Y-%M-%d"))

# set argparser
parser = argparse.ArgumentParser(description=PROG_DESCRIPTION, prog='cnpgen')
parser.add_argument(
    '--version',
    action='version',
    version=VERSION
)
parser.add_argument(
    '-c',
    action='store_true',
    default=False,
    help='Start new CNP wizard.',
)
parser.add_argument(
    '-g',
    metavar='amount',
    type=int,
    nargs=1,
    help='Generate random CNPs.'
)
parser.add_argument(
    '-i',
    metavar='CNP',
    type=str,
    nargs='+',
    help='Show CNP information.'
)

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

if args.c:
    print(
        'New CNP wizard.\n'
        'Please input required information. Defaults are in brackets.\n'
    )

    resident = True
    in_resident = input('Resident? [y/N]: ')
    if not len(in_resident) or in_resident == 'N' or in_resident == 'n':
        resident = False

    try:
        in_gender = input('Gender? [M]: ').upper()
        gender = Gender.M
        if len(in_gender):
            gender = Gender[in_gender]
    except KeyError:
        print('Value not allowed! Please use M or F. Default is M.')
        sys.exit(2)
    try:
        b_day = int(input('Birth day: '))
        b_month = int(input('Birth month: '))
        b_year = int(input('Birth year: '))
    except ValueError:
        print('Provided values for birth date are invalid. Must be numbers.')
        sys.exit(2)
    try:
        b_date = date(b_year, b_month, b_day)
    except ValueError:
        print('Invalid date.')
        sys.exit(2)
    try:
        region = Region[input('Region: ').title().replace('-', '_').replace(' ', '__')]
    except KeyError:
        print('Invalid region name.')
        sys.exit(2)
    try:
        serial = 1
        in_serial = input('Order number [1]: ')
        if len(in_serial):
            serial = int(in_serial)
    except ValueError:
        print('Serial must be number. Default is 1.')
        sys.exit(2)
    try:
        print(f'\nRESULT: {Cnp(gender, b_date, region, serial, resident)}')
    except Exception as err:
        print(err)
        sys.exit(2)

elif args.g:
    iterations = args.g[0]
    for _ in range(iterations):
        rand_gender = random.choice(list(Gender))
        rtime = MIN_D_DATE_TS + random.random() * (MAX_D_DATE_TS - MIN_D_DATE_TS)
        rand_b_date = date.fromtimestamp(rtime)
        rand_region = random.choice(list(Region))
        rand_serial = random.randint(1, 999)
        print(Cnp(rand_gender, rand_b_date, rand_region, rand_serial))

elif args.i:
    print("\n")
    header = 'CNP Information'
    print(header)
    for _cnp in args.i:
        print('=' * len(header))
        print(Cnp.info(_cnp), "\n")
else:
    parser.print_help()
    sys.exit(1)
