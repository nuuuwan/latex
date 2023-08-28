import os
import unittest

from latex import escape, escape_quotes, escape_url

DIR_TEST_OUTPUT = 'test_output'
TEST_TEX_PATH = os.path.join(DIR_TEST_OUTPUT, 'test.tex')


class TestCase(unittest.TestCase):
    def test_escape_url(self):
        for input, expected_output in [
            ['', ''],
            ['A', 'A'],
            ['https://www.xyz.com', '\\footnote{https://www.xyz.com}'],
            [
                'URL = https://www.xyz.com',
                'URL = \\footnote{https://www.xyz.com}',
            ],
            [
                'Url(https://www.xyz.com)',
                'Url(\\footnote{https://www.xyz.com})',
            ],
            [
                'Url(https://www.xyz.com/maps)',
                'Url(\\footnote{https://www.xyz.com/maps})',
            ],
            [
                'Url(https://www.xyz.com/maps?test=1)',
                'Url(\\footnote{https://www.xyz.com/maps?test=1})',
            ],
            [
                'Url(https://www.xyz.com/maps?v1=1&v2=2)',
                'Url(\\footnote{https://www.xyz.com/maps?v1=1&v2=2})',
            ],
        ]:
            actual_output = escape_url(input)
            self.assertEqual(actual_output, expected_output)

    def test_escape_quotes(self):
        for input, expected_output in [
            ['', ''],
            ['A', 'A'],
            ['Harry "The Hat" Anderson', 'Harry \\say{The Hat} Anderson'],
            ['"Hat Trick"', '\\say{Hat Trick}'],
            [
                '"Hat Trick" is a good book',
                '\\say{Hat Trick} is a good book',
            ],
            [
                '"Hat Trick" is a "good" book',
                '\\say{Hat Trick} is a \\say{good} book',
            ],
            ['James "Bubsy"', 'James \\say{Bubsy}'],
        ]:
            actual_output = escape_quotes(input)
            self.assertEqual(actual_output, expected_output)

    def test_escape(self):
        for input, expected_output in [
            ['A', 'A'],
            ['', ''],
            ['20%', '20\\%'],
            ['Tom & Jerry', 'Tom \\& Jerry'],
        ]:
            actual_output = escape(input)
            self.assertEqual(actual_output, expected_output)
