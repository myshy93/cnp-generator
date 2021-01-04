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
    def __init__(self, gender, year, month, day, region, serial=1, resident=False):
        self.gender = gender
        self.year = year
        self.month = month
        self.day = day
        self.region = region
        self.serial = serial
        self.resident = resident

    # TODO: validate dates

    def get_gender_code(self):
        """Calculate gender code based on gender, year and whether is resident or not.

        :raises ValueError: Invalid year was provided to constructor.
        :return: Gender code
        :rtype: int
        """
        if self.resident:
            gen_code = 7
        elif 1900 <= self.year <= 1999:
            gen_code = 1
        elif 1800 <= self.year <= 1899:
            gen_code = 3
        elif 2000 <= self.year <= 2099:
            gen_code = 5
        else:
            raise ValueError('Invalid year.')

        if self.gender == Gender.F:
            gen_code += 1

        return gen_code

    def get_partial(self):
        year_digits = [int(x) for x in str(self.year)]
        month_digits = [int(x) for x in str(self.month)]

        if len(year_digits) != 4:
            raise ValueError('Invalid year.')

        partial = [
            self.get_gender_code(),
            year_digits[-2],
            year_digits[-1],

        ]

        return partial


class Generator:
    pass


if __name__ == '__main__':
    cnp1 = Cnp(Gender.M, 2001, 10, 1, Region.Braila)
    print(cnp1.get_partial())
