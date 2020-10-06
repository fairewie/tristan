from django.test import TestCase

# Create your tests here.

class StringTest(TestCase):
    '''Test unitaire simple'''
    def test_concatene(self):
        self.assertEqual("Bon"+"jour","Bonjour")

