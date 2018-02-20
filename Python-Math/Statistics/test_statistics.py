import unittest
import logging
import sys
import statistics

logging.basicConfig(filename='statistics.log', level=logging.WARNING)


class TestStatistics(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n\tRunning Macro Setup...\n\n')

    @classmethod
    def tearDownClass(cls):
        print('\n\tRunning Macro Tear Down...\n')

    def setUp(self):
        print('\nRunning Micro Setup...\n')

    def tearDown(self):
        print('\nRunning Micro Tear Down...\n\n')


if __name__ == "__main__":
    unittest.main()
