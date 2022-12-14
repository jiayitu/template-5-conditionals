from unittest import TestCase

from bmi import calculate_bmi, bmi_to_category


class Test(TestCase):

    def test_calculate_bmi_1(self):
        length = 2
        weight = 70
        expected_bmi = 17.5

        bmi = calculate_bmi(length, weight)

        self.assertAlmostEqual(bmi, expected_bmi)

    def test_calculate_bmi_2(self):
        length = 2
        weight = 90
        expected_bmi = 22.5

        bmi = calculate_bmi(length, weight)

        self.assertAlmostEqual(bmi, expected_bmi)

    def test_calculate_bmi_3(self):
        length = 2
        weight = 110
        expected_bmi = 27.5

        bmi = calculate_bmi(length, weight)

        self.assertAlmostEqual(bmi, expected_bmi)

    def test_calculate_bmi_4(self):
        length = 2
        weight = 130
        expected_bmi = 32.5

        bmi = calculate_bmi(length, weight)

        self.assertAlmostEqual(bmi, expected_bmi)

    def test_bmi_category_15(self):
        bmi = 15
        expected_category = "underweight"

        category = bmi_to_category(bmi)

        self.assertEqual(expected_category, category)

    def test_bmi_category_22(self):
        bmi = 22
        expected_category = "healthy weight"

        category = bmi_to_category(bmi)

        self.assertEqual(expected_category, category)

    def test_bmi_category_27(self):
        bmi = 27
        expected_category = "overweight"

        category = bmi_to_category(bmi)

        self.assertEqual(expected_category, category)

    def test_bmi_category_32(self):
        bmi = 32
        expected_category = "obese"

        category = bmi_to_category(bmi)

        self.assertEqual(expected_category, category)
