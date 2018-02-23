from testlang2 import *
import unittest

url1 = 'http://live-igcommerce.pantheonsite.io/fr-fr/produit/outils-d-etalonnage/calibrateurs-de-pression/fluke-700g'
url2 = 'https://live-igcommerce.pantheonsite.io/cs-cz/produkt/kalibracni-pristroje/tlakove-kalibratory/fluke-700g'

class TestCase(unittest.TestCase):
	def test_is_french(self):
		self.assertEqual(is_background_color(url2), '#ffc20e')

	def test_is_background_color(self):
		self.assertEqual(is_Lang_by_id(url1), 'fr')

	def test_url_breadcrumb_matches(self):
		self.assertTrue(is_bread_crumb(url2))

if __name__ == '__main__':
    unittest.main()