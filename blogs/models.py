from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    post = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True)


class Post(models.Model):
    title = models.CharField(max_length=100)
