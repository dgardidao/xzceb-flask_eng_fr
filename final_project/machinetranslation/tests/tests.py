import unittest
from translator import french_to_english, english_to_french

class TestProject(unittest.TestCase):

	def test_french_to_english_with_null_input(self):
    		# Test the frenchToEnglish function with null input
    		self.assertTrue(french_to_english(None) == None)

	def test_english_to_french_with_null_input(self):
    		# Test the englishToFrench function with null input
    		self.assertTrue(english_to_french(None) == None)

	def test_french_to_english_with_bonjour_input(self):
    		# Test the frenchToEnglish function with "Bonjour" input
    		french_text = "Bonjour"
    		expected_output = "Hello"
    		self.assertEqual(french_to_english(french_text), expected_output)

	def test_english_to_french_with_hello_input(self):
    		# Test the englishToFrench function with "Hello" input
    		english_text = "Hello"
    		expected_output = "Bonjour"
    		self.assertEqual(english_to_french(english_text), expected_output)

unittest.main()
