from django.db import models


class TestModel(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=10)
    age = models.IntegerField()


class Example(models.Model):
    integer_field = models.IntegerField()
    positive_field = models.PositiveIntegerField()
    positive_small_field = models.PositiveSmallIntegerField()
    big_integer_field = models.BigIntegerField()
    float_field = models.FloatField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=5)
    text_field = models.TextField(max_length=20)
    date_field = models.DateField(auto_now=False, auto_now_add=False)
    date_time_field = models.DateTimeField(auto_now_add=False)
    decimal_field = models.DecimalField(max_digits=8, decimal_places=2) #222222.22
    email = models.EmailField()
    file_field = models.FileField(upload_to='file')
    image_field = models.ImageField(upload_to='images')


class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя", blank=True)
    surname = models.CharField(max_length=50, verbose_name="Фамилия")
    date_birth = models.DateField(auto_now=False, verbose_name="Дата рождения")

    def __str__(self):
        return self.name + ' ' + self.surname


class Book(models.Model):

    CHOISE_GENRE = (
        ('comedy', "Comedy"),
        ('tragedy', "Tragedy"),
        ('drama', "Drama"),
    )

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)
    genre = models.CharField(max_length=50, choices=CHOISE_GENRE)


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return self.place


class Publication(models.Model):
    title = models.CharField(max_length=30)

    # def __str__(self):
    #     return self.title
    #
    # class Meta:
    #     ordering = ('title', )


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    # def __str__(self):
    #     return self.headline
    #
    class Meta:
        ordering = ('headline', )
