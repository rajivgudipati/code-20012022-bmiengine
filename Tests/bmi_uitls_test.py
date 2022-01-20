from utils import bmi_utils
import pandas as pd
import unittest

'''Note: Due to lack of time I could not able to write unittest for all functions.
I was completely occupied in my project related activities. Sorry about that'''

class TestBMIUTils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sample_json = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }]

    def test_convert_json_to_dataframe(self):
        act_output = bmi_utils.convert_json_to_dataframe(self.sample_json)
        expected_output = 1

        self.assertEqual(len(act_output), expected_output)


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    all_test_cases = loader.loadTestsFromTestCase(TestBMIUTils)
    suite.addTests(all_test_cases)
    runner = unittest.TextTestRunner()
    runner.run(suite)


