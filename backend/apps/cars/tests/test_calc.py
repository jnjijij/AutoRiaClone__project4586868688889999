from unittest import TestCase

from apps.cars.services import calc


class CalcTestCase(TestCase):
    def test_plus(self):
        res = calc(1, 2, "+")
        self.assertEquals(res, 3)

    def test_minus(self):
        res = calc(1, 2, "-")
        self.assertEquals(res, -1)

    def test_multi(self):
        res = calc(1, 2, "*")
        self.assertEquals(res, 2)
