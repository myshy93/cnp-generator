from datetime import datetime
from unittest import TestCase

from cnpgen import Cnp, Gender, Region


class TestCnp(TestCase):

    def setUp(self) -> None:
        self.dummy_date1 = datetime(2001, 10, 1)
        self.dummy_date2 = datetime(1993, 10, 1)
        self.dummy_date3 = datetime(1999, 10, 1)
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
        # resident
        cnp7 = Cnp(Gender.F, self.dummy_date1, Region.Braila, resident=True)
        cnp8 = Cnp(Gender.M, self.dummy_date3, Region.Braila, resident=True)

        self.assertEqual(cnp1.get_gender_code(), 5)
        self.assertEqual(cnp2.get_gender_code(), 6)
        self.assertEqual(cnp3.get_gender_code(), 1)
        self.assertEqual(cnp4.get_gender_code(), 2)
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

    def test_partial(self):
        cnp = Cnp(Gender.M, datetime(1993, 8, 2), Region.Braila, serial=2)
        partial = cnp.partial
        self.assertEqual(len(partial), 12)
        self.assertEqual(int(partial[0]), 1)
        self.assertEqual(int(partial[1]), 9)
        self.assertEqual(int(partial[2]), 3)
        self.assertEqual(int(partial[3]), 0)
        self.assertEqual(int(partial[4]), 8)
        self.assertEqual(int(partial[5]), 0)
        self.assertEqual(int(partial[6]), 2)
        self.assertEqual(int(partial[7]), 0)
        self.assertEqual(int(partial[8]), 9)
        self.assertEqual(int(partial[9]), 0)
        self.assertEqual(int(partial[10]), 0)
        self.assertEqual(int(partial[11]), 2)

        cnp2 = Cnp(Gender.F, datetime(2001, 12, 12), Region.Braila)
        partial2 = cnp2.partial
        self.assertEqual(len(partial2), 12)
        self.assertEqual(int(partial2[0]), 6)
        self.assertEqual(int(partial2[1]), 0)
        self.assertEqual(int(partial2[2]), 1)
        self.assertEqual(int(partial2[3]), 1)
        self.assertEqual(int(partial2[4]), 2)
        self.assertEqual(int(partial2[5]), 1)
        self.assertEqual(int(partial2[6]), 2)
        self.assertEqual(int(partial2[7]), 0)
        self.assertEqual(int(partial2[8]), 9)
        self.assertEqual(int(partial2[9]), 0)
        self.assertEqual(int(partial2[10]), 0)
        self.assertEqual(int(partial2[11]), 1)

    def test_compute_c(self):
        self.assertEqual(Cnp.compute_c('506060251001'), 4)
        self.assertEqual(Cnp.compute_c('616062122001'), 4)

        with self.assertRaises(TypeError):
            Cnp.compute_c('245432')

        with self.assertRaises(ValueError):
            Cnp.compute_c('61606212200q')

        self.assertEqual(Cnp.compute_c('001100000000'), 1)

    def test_full(self):
        cnp = Cnp(Gender.M, datetime(1993, 3, 2), Region.Iasi, serial=22)
        self.assertEqual(len(cnp.full), Cnp.LENGTH)
        self.assertEqual(cnp.full, '1930302220223')
        cnp2 = Cnp(Gender.M, datetime(2006, 6, 2), Region.Calarasi)
        self.assertEqual(cnp2.full, '5060602510014')

    def test_is_valid(self):
        self.assertTrue(Cnp.is_valid('1930302220223'))
        self.assertFalse(Cnp.is_valid(1923456))
        self.assertFalse(Cnp.is_valid('1923456'))
        self.assertFalse(Cnp.is_valid(None))
        self.assertFalse(Cnp.is_valid('1930302220224'))
