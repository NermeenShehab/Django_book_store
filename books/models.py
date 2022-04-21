import datetime
from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=70)
    publish_date = models.DateField()
    add_to_site_at = models.DateField()
    price = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    appropriate = models.CharField(max_length=30)
    # image = models.ImageField(upload_to="books/static/images")
    image = models.ImageField()

    def __str__(self):
        return self.name
