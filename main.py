from datetime import datetime
from enum import Enum


class Gender(Enum):
    M = 1
    F = 2


class Region(Enum):
    Alba = 1
    Arad = 2
    Arges = 3
    Bacau = 4
    Bihor = 5
    Bistrita_Nasaud = 6
    Botosani = 7
    Brasov = 8
    Braila = 9
    Buzau = 10
    Caras_Severin = 11
    Cluj = 12
    Constanta = 13
    Covasna = 14
    Dambovita = 15
    Dolj = 16
    Galati = 17
    Gorj = 18
    Hargita = 19
    Hunedoara = 20
    Ialomita = 21
    Iasi = 22
    Ilfov = 23
    Maramures = 24
    Mehedinti = 25
    Mures = 26
    Neamt = 27
    Olt = 28
    Prahova = 29
    Satu_Mare = 30
    Salaj = 31
    Sibiu = 32
    Suceava = 33
    Teleorman = 34
    Timis = 35
    Tulcea = 36
    Vaslui = 37
    Valcea = 38
    Vrancea = 39
    Bucuresti = 40
    Bucuresti_Sector__1 = 41
    Bucuresti_Sector__2 = 42
    Bucuresti_Sector__3 = 43
    Bucuresti_Sector__4 = 44
    Bucuresti_Sector__5 = 45
    Bucuresti_Sector__6 = 46
    Calarasi = 51
    Giurgiu = 52


class Cnp:

    LENGTH = 13
    PARTIAL_LENGTH = LENGTH - 1
    REF_CONSTANT = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]

    def __init__(self, gender, birth_date, region, serial=1, resident=False):

        # sanity checks
        if not isinstance(gender, Gender):
            raise TypeError('Gender in not a gender object.')

        if not isinstance(birth_date, datetime):
            raise TypeError('Birth date is not a datetime object.')

        if not isinstance(region, Region):
            raise TypeError('Region is not a Region object.')

        if not isinstance(serial, int) or serial > 1000 or serial < 1:
            raise TypeError('Invalid serial. Must be a int in range 1-999.')

        if not isinstance(resident, bool):
            raise TypeError('Residential state should be bool.')

        self.gender = gender
        self.birth_date = birth_date
        self.region = region
        self.serial = serial
        self.resident = resident

    def get_gender_code(self):
        """Calculate gender code based on gender, year and whether is resident or not.

        :raises ValueError: Invalid year was provided to constructor.
        :return: Gender code
        :rtype: int
        """
        if self.resident:
            gen_code = 7
        elif 1900 <= self.birth_date.year <= 1999:
            gen_code = 1
        elif 1800 <= self.birth_date.year <= 1899:
            gen_code = 3
        elif 2000 <= self.birth_date.year <= 2099:
            gen_code = 5
        else:
            raise ValueError('Year is out of range.')

        if self.gender == Gender.F:
            gen_code += 1

        return gen_code

    @property
    def partial(self):
        """Put together first 12 digits of CNP based on CNP standard.
        :return: First 12 digits of CNP.
        :rtype: str
        """
        return "".join([
            str(self.get_gender_code()),
            self.birth_date.strftime("%y"),
            self.birth_date.strftime("%m"),
            self.birth_date.strftime("%d"),
            f"{self.region.value:0>2}"
            f"{self.serial:0>3}",
        ])

    @property
    def full(self):
        """Full CNP as string.
        :return: Full CNP as string.
        :rtype: str
        """
        return f"{self.partial}{self.compute_c(self.partial)}"

    @staticmethod
    def compute_c(partial):
        """Compute check digit for a partial CNP (12 digits).
        :param partial: Partial CNP to check.
        :type partial: str
        :return: Calculated control digit.
        :rtype: int
        """
        if not isinstance(partial, str) or len(partial) != Cnp.PARTIAL_LENGTH:
            raise TypeError("Invalid partial CNP, expected a string with length 12.")

        digits = [int(x) for x in partial if x.isdigit()]

        if len(digits) != len(partial):
            raise ValueError('Partial must contain only digits!')

        step1 = [digits[i] * Cnp.REF_CONSTANT[i] for i in range(len(digits))]
        step2 = sum(step1) % 11

        if step2 < 10:
            return step2
        else:
            return 1

    @staticmethod
    def is_valid(_cnp):
        """Check CNP validity.
        :param _cnp: CNP to check.
        :type _cnp: str
        :return: True if CNP is valid of False if not.
        :rtype: bool
        """
        if isinstance(_cnp, str) and len(_cnp) == Cnp.LENGTH:
            partial = _cnp[:-1]
            if int(_cnp[-1]) == Cnp.compute_c(partial):
                return True
        return False



class Generator:
    pass


if __name__ == '__main__':
    cnp1 = Cnp(Gender.F, datetime(2016, 6, 21), Region.Iasi)
    print(cnp1.full)
