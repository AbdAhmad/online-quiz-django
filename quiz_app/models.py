from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    quiz_name = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quiz_name

    class Meta:
        verbose_name_plural = 'Quizes'


class Question(models.Model):
    question = models.CharField(max_length=200, unique=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    option_one = models.CharField(max_length=100)
    option_two = models.CharField(max_length=100)
    option_three = models.CharField(max_length=100)
    option_four = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    bio = models.CharField(max_length=250)  

    def __str__(self):
        return self.user.username




