from django.test import TestCase, SimpleTestCase
from django.urls import reverse

class Snacks_Tests(TestCase):
    def test_snacks_page(self):
        url = reverse('Snacks')
        actual = self.client.get(url).status_code
        expected = 200
        self.assertEqual(actual, expected)
    def test_page_templete(self):
        url = reverse('Snacks')
        actual = self.client.get(url)
        expected='snacks.html'
        self.assertTemplateUsed(actual,expected) 