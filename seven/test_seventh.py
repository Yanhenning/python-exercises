from unittest import TestCase

from seven.seventh import getMaxValue


class GetMaxValueTests(TestCase):
    def test_return_max_value(self):
        carrotTypes = [
            {'kg': 5, 'price': 100},
            {'kg': 7, 'price': 150},
            {'kg': 3, 'price': 70},
        ]

        max_value = getMaxValue(carrotTypes, 36)

        self.assertEqual(750, max_value)
