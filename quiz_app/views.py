# from django.db.models.query_utils import Q
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Quiz, Question, Profile
from .forms import QuestionForm, QuizForm, EditProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if len(password1) < 8:
            messages.error(request, 'Password is too short')
            return redirect('signup')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username is already taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(first_name=first_name, email=email, username=username, password=password1)
                user.save()
                username = request.POST['username']
                password1 = request.POST['password1']
                user = auth.authenticate(username=username, password=password1)
                auth.login(request, user)
                messages.success(request, 'Signup was successful')
                return redirect('/')
        else:
            messages.error(request, "Two passwords didn't match")
            return redirect('signup')

    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'quiz_app/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Welcome ' + username)
            return redirect('welcome')
        else:
            messages.error(request, 'Wrong credentials')
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'quiz_app/login.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('welcome')


def welcome(request):
    if request.method == 'POST':
        return redirect('/') 
    else:
        return render(request, 'quiz_app/welcome.html')


def quizes(request):
    quizes = Quiz.objects.all()
    return render(request, 'quiz_app/quizes.html', {'quizes': quizes})


def quiz(request, id):
    questions = Question.objects.filter(quiz=id)   
    return render(request, 'quiz_app/quiz.html', {'questions': questions})


@login_required
def create_quiz(request):
    if request.method == 'POST':
        quiz_form = QuizForm(request.POST)
        if quiz_form.is_valid():
            quiz = quiz_form.save(commit=False)
            quiz.author = request.user
            quiz.save()
            messages.success(request, 'Quiz created succesfully')
            redirect('create_question')
    else:
        quiz_form = QuizForm()
    return render(request, 'quiz_app/create_quiz.html', {'quiz_form': quiz_form})


@login_required
def create_question(request):
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question_form.save()
            messages.success(request, 'Question added succesfully')
            return redirect('create_question')
    else:
        question_form = QuestionForm()
    return render(request, 'quiz_app/create_question.html', {'question_form': question_form})


@login_required
def my_quizes(request):
    user = request.user
    my_quizes = Quiz.objects.filter(author=user)
    return render(request, 'quiz_app/my_quizes.html', {'my_quizes': my_quizes})


@login_required
def profile_page(request):
    user = request.user
    quizes = Quiz.objects.filter(author=user)
    quizes_count = quizes.count()
    profile = Profile.objects.get(user=user)
    return render(request, 'quiz_app/profile.html', {'user': user, 'quizes_count': quizes_count, 'profile': profile})


@login_required
def edit_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()          
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')

    return render(request, 'quiz_app/edit_profile.html', {'profile': profile, 'form': form})


@login_required
def edit_quiz(request, pk):
    quiz = Quiz.objects.get(id=pk)
    if request.method == 'GET':
        quiz_form = QuizForm(instance=quiz)
    else:  # POST
        quiz_form = QuizForm(request.POST, instance=quiz)
        if quiz_form.is_valid():
            quiz_form.save()
            messages.success(request, 'Quiz updated successfully')
            return redirect('my_quizes')
            
    return render(request, 'quiz_app/create_quiz.html', {'quiz_form': quiz_form})


@login_required
def delete_quiz(request, pk):
    quiz = Quiz.objects.get(id=pk)
    quiz.delete()
    return redirect('/')


@login_required
def edit_question(request, id):
    question = Question.objects.get(id=id)
    if request.method == 'GET':
        question_form = QuestionForm(instance=question)
    else:  # POST
        question_form = QuestionForm(request.POST, instance=question)
        if question_form.is_valid():
            question_form.save()
            messages.success(request, 'Post updated successfully')
            return redirect('my_quizes')
            
    return render(request, 'quiz_app/create_question.html', {'question_form': question_form})


@login_required
def my_questions(request):
    user = request.user
    my_questions = Question.objects.filter(author=user)
    return render(request, 'quiz_app/my_questions.html', {'my_questions': my_questions})