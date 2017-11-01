import unittest


class EightQueensTests(unittest.TestCase):
    def test(self, size=8):
        geneset = [i for i in range(size)]
