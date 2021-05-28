from django import forms
# from django.forms import fields
from .models import Quiz, Question, Profile

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['quiz_name']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'quiz', 'option_one', 'option_two', 'option_three', 'option_four', 'answer']


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['location', 'bio']