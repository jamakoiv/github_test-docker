#!/usr/bin/python3

import unittest
import datetime
import sys
sys.path.append("src")

from TimeHasher import TimeHasher

class TestTimeHasher(unittest.TestCase):

    test_now = datetime.datetime(2000, 1, 2, 3, 4, 5)

    def test_HashNow_MD5(self):
        target = '3e7d29cec9449c6e41859fedb3af90ce'

        settings = {'hash_algorithm': 'md5',
                    'string_encoding': 'utf-8'}

        hasher = TimeHasher(settings)
        self.assertEqual(hasher.HashDatetime(self.test_now), target)

    def test_HashNow_SHA1(self):
        target = 'bc7d5905308d0081c032589bec098b27771c3c6e'
        settings = {'hash_algorithm': 'sha1',
                    'string_encoding': 'utf-8'}

        hasher = TimeHasher(settings)
        self.assertEqual(hasher.HashDatetime(self.test_now), target)


if __name__ == "__main__":
    unittest.main()