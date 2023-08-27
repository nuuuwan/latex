import os
import unittest

from latex import Chapter, Items, Label, LatexBook, Part, Ref, Section

DIR_TEST_OUTPUT = 'test_output'
TEST_TEX_PATH = os.path.join(DIR_TEST_OUTPUT, 'test.tex')


class TestCase(unittest.TestCase):
    def test_init(self):
        latex_book = LatexBook(
            'Test Books',
            Part(
                'The Beginning',
                Chapter('Help', Label('Help')),
            ),
            Part(
                'The End',
                Chapter(
                    'Cats',
                    Section('Meow', Items('Hello', 'World', Ref('Help'))),
                ),
            ),
        )

        latex_book.write(TEST_TEX_PATH)
        self.assertTrue(os.path.exists(TEST_TEX_PATH))
