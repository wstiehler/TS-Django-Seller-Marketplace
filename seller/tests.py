from django.test import TestCase

# Create your tests here.
class TestSellerViews(TestCase):

    def test_page_init(self):
        result = self.client.get('')
        self.assertEqual(result.status_code, 200)
        self.assertTemplateUsed(result, 'index.html')

    def test_page_seller(self):
        result = self.client.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertTemplateUsed(result, 'seller.html')