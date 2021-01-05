from datetime import datetime
from unittest import TestCase

from main import Cnp, Gender, Region


class TestCnp(TestCase):

    def setUp(self) -> None:
        self.dummy_date1 = datetime(2001, 10, 1)
        self.dummy_date2 = datetime(1993, 10, 1)
        self.dummy_date3 = datetime(1999, 10, 1)
        self.dummy_date4 = datetime(1895, 10, 1)
        self.dummy_date5 = datetime(1877, 10, 1)
        self.out_range_date = datetime(1700, 1, 2)
        self.out_range_date2 = datetime(2200, 1, 2)

    def test_constructor(self):
        with self.assertRaises(TypeError):
            Cnp(1, self.dummy_date1, Region.Covasna)

        with self.assertRaises(TypeError):
            Cnp(Gender.F, None, Region.Giurgiu)

        with self.assertRaises(TypeError):
            Cnp(Gender.F, self.dummy_date1, None)

        with self.assertRaises(TypeError):
            Cnp(Gender.F, self.dummy_date1, Region.Braila, 2222)

        with self.assertRaises(TypeError):
            Cnp(Gender.F, self.dummy_date1, Region.Braila, 0)

        with self.assertRaises(TypeError):
            Cnp(Gender.F, self.dummy_date1, Region.Braila, '223')

        with self.assertRaises(TypeError):
            Cnp(Gender.F, self.dummy_date1, Region.Braila, 2, None)

        Cnp(Gender.F, self.dummy_date1, Region.Braila)

    def test_get_gender_code(self):
        cnp1 = Cnp(Gender.M, self.dummy_date1, Region.Braila)
        cnp2 = Cnp(Gender.F, self.dummy_date1, Region.Braila)
        cnp3 = Cnp(Gender.M, self.dummy_date2, Region.Braila)
        cnp4 = Cnp(Gender.F, self.dummy_date3, Region.Braila)
        cnp5 = Cnp(Gender.M, self.dummy_date4, Region.Braila)
        cnp6 = Cnp(Gender.F, self.dummy_date5, Region.Braila)
        # resident
        cnp7 = Cnp(Gender.F, self.dummy_date1, Region.Braila, resident=True)
        cnp8 = Cnp(Gender.M, self.dummy_date3, Region.Braila, resident=True)

        self.assertEqual(cnp1.get_gender_code(), 5)
        self.assertEqual(cnp2.get_gender_code(), 6)
        self.assertEqual(cnp3.get_gender_code(), 1)
        self.assertEqual(cnp4.get_gender_code(), 2)
        self.assertEqual(cnp5.get_gender_code(), 3)
        self.assertEqual(cnp6.get_gender_code(), 4)
        self.assertEqual(cnp7.get_gender_code(), 8)
        self.assertEqual(cnp8.get_gender_code(), 7)

        with self.assertRaises(ValueError):
            Cnp(
                Gender.F,
                self.out_range_date,
                Region.Covasna
            ).get_gender_code()
            Cnp(
                Gender.F,
                self.out_range_date2,
                Region.Covasna
            ).get_gender_code()
