from django.db import models


class House(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=100)
    image = models.CharField(max_length=500)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class User(models.Model):
    pass