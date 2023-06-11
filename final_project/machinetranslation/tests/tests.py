import unittest
from translator import english_to_french, french_to_english

class TestModule(unittest.TestCase):
    
    def test_english_to_french(self):
        self.assertEqual(english_to_french('hello'), 'bonjour')
        self.assertEqual(english_to_french('good'), 'bien')
        self.assertEqual(english_to_french('bad'), 'mauvais')
        self.assertEqual(english_to_french('goodbye'), 'au revoir')
        self.assertNotEqual(english_to_french('hello'), 'salut')
        self.assertNotEqual(english_to_french('good'), 'parfait')
        self.assertNotEqual(english_to_french('evil'), 'Mauvais')
        self.assertNotEqual(english_to_french('goodbye'), 'Adieu')
    
    def test_french_to_english(self):
        self.assertEqual(french_to_english('bonjour'), 'hello')
        self.assertEqual(french_to_english('bien'), 'good')
        self.assertEqual(french_to_english('mauvais'), 'bad')
        self.assertEqual(french_to_english('au revoir'), 'goodbye')
        self.assertNotEqual(french_to_english('salut'), 'hello')
        self.assertNotEqual(french_to_english('parfeit'), 'good')
        self.assertNotEqual(french_to_english('evil'), 'Mauvais')
        self.assertNotEqual(french_to_english('goodbye'), 'Adieu')

if __name__ == '__main__':
    unittest.main()