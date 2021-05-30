from django import forms
from .models import Quiz, Question, Profile
from crispy_forms.helper import FormHelper

class QuizForm(forms.ModelForm):

    quiz_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Quiz Name'})
    )

    class Meta:
        model = Quiz
        fields = ['quiz_name']

    helper = FormHelper()
    helper.form_show_labels = False


class QuestionForm(forms.ModelForm):

    question = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Question'})
    )

    option_one = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Option One'})
    )

    option_two = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Option Two'})
    )

    option_three = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Option Three'})
    )
    

    option_four = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Option Four'})
    )

    answer = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Answer'})
    )

    class Meta:
        model = Question
        fields = ['question', 'quiz', 'option_one', 'option_two', 'option_three', 'option_four', 'answer']

    helper = FormHelper()
    helper.form_show_labels = False


class EditProfileForm(forms.ModelForm):

    location = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Location'})
    )

    bio = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Bio'})
    )

    class Meta:
        model = Profile
        fields = ['location', 'bio']

    helper = FormHelper()
    helper.form_show_labels = False

