from django.core.management.base import BaseCommand
import pandas as pd

from lesson_nine import models


class ErrorInFileFormat(Exception):

    def __str__(self):
        return 'You have some error in data format. You need something like this \n \
               "name,description,image,price,rating,slug,category,in_stock" \n \
               name, description, image, price, rating, category, in_stock - are required fields'


class ImageFormatError(Exception):

    def __str__(self):
        return 'Your image should be in images dir: \
               images/YOUR_FILE'


def parse_image_format(image):
    if not image:
        raise ErrorInFileFormat
    path = image.split('/')
    if len(path) != 2:
        raise ImageFormatError
    if path[0] != 'images':
        raise ImageFormatError


class Command(BaseCommand):

    help = 'This command get data from csv file and save it to base'

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name', type=str, help='The csv file that contains the product info'
        )

    def handle(self, *args, **kwargs):
        # kwargs = {
        #     'file_name': 'base.csv'
        # }
        file_name = kwargs['file_name']
        df = pd.read_csv(file_name)
        for idx, value in df.iterrows():
            try:
                category = models.Categories.objects.get(slug=value['category'])
            except:
                raise ErrorInFileFormat

            parse_image_format(value['image'])

            try:
                product = models.Product.objects.create(name=value['name'],
                                                        description=value['description'],
                                                        image=value['image'],
                                                        price=value['price'],
                                                        rating=value['rating'],
                                                        slug=value['slug'],
                                                        category=category,
                                                        in_stock=value['in_stock'])
            except:
                raise ErrorInFileFormat

            product.save()
            print('"{}" - SUCCESS saved'.format(product))