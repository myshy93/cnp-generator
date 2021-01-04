from unittest import TestCase

from main import Cnp, Gender, Region


class TestCnp(TestCase):

    def setUp(self) -> None:
        self.cnp1 = Cnp(Gender.M, 2001, 10, 1, Region.Braila)
        self.cnp2 = Cnp(Gender.F, 2001, 10, 1, Region.Braila)
        self.cnp3 = Cnp(Gender.M, 1993, 10, 1, Region.Braila)
        self.cnp4 = Cnp(Gender.F, 1999, 10, 1, Region.Braila)
        self.cnp5 = Cnp(Gender.M, 1895, 10, 1, Region.Braila)
        self.cnp6 = Cnp(Gender.F, 1877, 10, 1, Region.Braila)
        # resident
        self.cnp7 = Cnp(Gender.F, 2001, 1, 1, Region.Braila, resident=True)
        self.cnp8 = Cnp(Gender.M, 1999, 1, 1, Region.Braila, resident=True)

    def test_get_gender_code(self):
        self.assertEqual(self.cnp1.get_gender_code(), 5)
        self.assertEqual(self.cnp2.get_gender_code(), 6)
        self.assertEqual(self.cnp3.get_gender_code(), 1)
        self.assertEqual(self.cnp4.get_gender_code(), 2)
        self.assertEqual(self.cnp5.get_gender_code(), 3)
        self.assertEqual(self.cnp6.get_gender_code(), 4)
        self.assertEqual(self.cnp7.get_gender_code(), 8)
        self.assertEqual(self.cnp8.get_gender_code(), 7)

        with self.assertRaises(ValueError):
            Cnp(
                Gender.F,
                210,
                1,
                1,
                Region.Covasna
            ).get_gender_code()
