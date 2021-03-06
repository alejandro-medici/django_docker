from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    director = models.CharField(max_length=200)
    rating = models.IntegerField()
