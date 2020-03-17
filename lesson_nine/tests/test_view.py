from django.test import TestCase
from django.urls import reverse

from lesson_nine import views, models


class ProductListTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        prod_count = 13
        for prod_num in range(prod_count):
            if prod_num == 10:
                name = 'search_testing'
            else:
                name = 'test_name_{}'.format(prod_num)
            models.Product.objects.create(name=name,
                                          description='test_descr_{}'.format(prod_num),
                                          price=prod_num,
                                          image='images/unnamed.jpg')

    def test_product_list_url(self):
        resp = self.client.get(reverse('product_list_url'))
        self.assertEqual(resp.status_code, 200)

    def test_product_list_template(self):
        resp = self.client.get(reverse('product_list_url'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'lesson_nine/products_list.html')

    def test_product_list_result(self):
        resp = self.client.get(reverse('product_list_url'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.context['object_list']), 13)

    def test_filter_list(self):
        resp = self.client.get(reverse('product_list_url'), {'search': 'search_testing'})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.context['object_list']), 1)

    def test_search_form(self):
        resp = self.client.get(reverse('product_list_url'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, '<input type="text" name="search_field"')

