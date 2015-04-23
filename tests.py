import unittest

from pydna import seq_utils


class TestSeqUtils(unittest.TestCase):
    def test_is_codon_correct(self):
        codon = 'ACG'
        result = seq_utils.is_codon_correct(codon)
        expected = True
        self.assertEqual(expected, result)
        
    def test_is_codon_correct_bad_codon_symbol(self):
        codon = 'A$G'
        result = seq_utils.is_codon_correct(codon)
        expected = False
        self.assertEqual(expected, result) 
        
    def test_is_codon_correct_bad_codon_number(self):
        codon = 314
        result = seq_utils.is_codon_correct(codon)
        expected = False
        self.assertEqual(expected, result) 
