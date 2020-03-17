from django.test import TestCase

from lesson_nine import models


#https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Testing


# class TestTest(TestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#         print('Here in setUpTest Data')
#
#     def setUp(self) -> None:
#         print('Here un setUp')
#
#     def test_false_is_false(self):
#         print("Method: test_false_is_false.")
#         self.assertFalse(False)
#
#     def test_false_is_true(self):
#         print("Method: test_false_is_true.")
#         self.assertTrue(False)
#
#     def test_one_plus_one_equals_two(self):
#         print("Method: test_one_plus_one_equals_two.")
#         self.assertEqual(1 + 1, 2)
#
#     def tearDown(self) -> None:
#         print('Here in tear down')
#
#     @classmethod
#     def tearDownClass(cls):
#         print('Here in tear donw class')


class MainModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.category_name = 'Test category'
        models.Categories.objects.create(category_name=cls.category_name)

        cls.product_obj = models.Product.objects.create(name='Test prod',
                                                        description='test descr',
                                                        price=1,
                                                        image='images/unnamed.jpg'
                                                        )

        models.Review.objects.create(product=cls.product_obj, rating=4, text='first review')
        models.Review.objects.create(product=cls.product_obj, rating=4, text='second review')

    def test_category_slug(self):
        category = models.Categories.objects.get(category_name=self.category_name)
        slug = category.slug
        self.assertEqual(slug, 'test-category')

    def test_product_count_comments(self):
        review_number = self.product_obj.count_comments()
        self.assertEqual(review_number, 2)

    @classmethod
    def tearDownClass(cls):
        models.Categories.objects.get(category_name=cls.category_name).delete()
