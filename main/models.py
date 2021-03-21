from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Fact(models.Model):
    phrase = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    popularity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.category) + ', ' + str(self.phrase) + ', ' + str(self.popularity)
