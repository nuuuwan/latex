import os
import unittest

from utils import File

from latex import (Bold, Chapter, Color, Index, Italic, Items, Join, Label,
                   LatexBook, Part, Ref, Section, Str)

DIR_TEST_OUTPUT = 'output'
TEST_TEX_PATH = os.path.join(DIR_TEST_OUTPUT, 'test.tex')
EXPECTED_TEX_PATH = os.path.join('tests', 'expected_test.tex')


class TestCase(unittest.TestCase):
    def test_init(self):
        latex_book = LatexBook(
            'Test Books',
            'Test Author',
            Part(
                'The Beginning',
                Chapter('Help', Label('Help')),
            ),
            Part(
                'The End',
                Chapter(
                    'Cats',
                    Join(
                        Str('What'),
                        Str('color is'),
                        Str('the'),
                        Bold(Str('cat?')),
                    ),
                    Color('red', Str('Red!!!')),
                    Section(
                        'Meow',
                        Items(
                            Str('Hello'),
                            Italic(Str('World')),
                            Ref('Help'),
                            Index('Help'),
                        ),
                    ),
                ),
            ),
        )

        latex_book.write(TEST_TEX_PATH)
        self.assertTrue(os.path.exists(TEST_TEX_PATH))
        self.assertEqual(
            File(TEST_TEX_PATH).read(),
            File(EXPECTED_TEX_PATH).read(),
        )
