import unittest

from similarity_checker import SimilarityChecker


class TestSimilarityChecker(unittest.TestCase):

    def test_num_char_score(self):
        sc = SimilarityChecker()
        sc.set_strings("ASD", "DSA")
        self.assertEqual(sc.get_score1(), 60)
        sc.set_strings("A", "BB")
        self.assertEqual(sc.get_score1(), 0)
        sc.set_strings("AAABB", "BAA")
        self.assertEqual(sc.get_score1(), 20.0)
        sc.set_strings("AA", "AAE")
        self.assertEqual(sc.get_score1(), 30.0)

    def test_appear_char_score(self):
        sc = SimilarityChecker()
        sc.set_strings("ASD", "DSA")
        self.assertEqual(sc.get_score2(), 40)
        sc.set_strings("A", "BB")
        self.assertEqual(sc.get_score2(), 0)
        sc.set_strings("AAABB", "BAA")
        self.assertEqual(sc.get_score2(), 40)
        sc.set_strings("AA", "AAE")
        self.assertEqual(sc.get_score2(), 20)
        self.assertEqual(sc.get_score2(), 30)
