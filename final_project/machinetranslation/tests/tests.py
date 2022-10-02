import unittest

from translator import english_to_french, french_to_english

class TestMachineTranslation(unittest.TestCase):
    def test_null_english_to_french(self):
        self.assertEqual(english_to_french('Null'), 'Null')
        
    def test_null_french_to_english(self):
        self.assertEqual(french_to_english('Null'), 'Null')
        
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')


if __name__ == "__main__":
    unittest.main()
