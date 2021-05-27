from django.db import models

# Create your models here.

class Quiz(models.Model):
    quiz_name = models.CharField(max_length=100, unique=True)
    number_of_questions = models.IntegerField()

    def __str__(self):
        return self.quiz_name

    class Meta:
        verbose_name_plural = 'Quizes'

class Question(models.Model):
    question = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    option_one = models.CharField(max_length=100)
    option_two = models.CharField(max_length=100)
    option_three = models.CharField(max_length=100, blank=True)
    option_four = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.question
