from django.db.models.query_utils import Q
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Quiz, Question
from django.http import JsonResponse
from .forms import QuestionForm, QuizForm

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
            return redirect('/')
        else:
            messages.error(request, 'Wrong credentials')
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'quiz_app/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def index(request):
    if request.method == 'POST':
        return redirect('/')
    else:
        return render(request, 'quiz_app/index.html')

def quizes(request):
    quizes = Quiz.objects.all()
    return render(request, 'quiz_app/quizes.html', {'quizes': quizes})

def quiz(request, id):
    raw_questions = Question.objects.filter(quiz=id)
    questions = []
    for raw_question in raw_questions:
        question = {}
        question['question'] = raw_question.question
        question['answer'] = raw_question.answer
        options = []
        options.append(raw_questions.option_one)
        options.append(raw_questions.two)
        options.append(raw_questions.three)
        options.append(raw_questions.four)
        question.append(options)
        questions.append(question)
    return JsonResponse(questions)
        
    # questions = Question.objects.filter()
    # questions = []
    # for question in quiz:
    #     answers = []
    #     for answer in question:
    #         answers.append(answer.answer)
    #     questions.append({str(question): answers})
   
    return render(request, 'quiz_app/quiz.html', {'questions': questions})


def create_quiz(request):
    if request.method == 'POST':
        quiz_form = QuizForm(request.POST)
        if quiz_form.is_valid():
            quiz_form.save()
            redirect('create_questions')
    else:
        quiz_form = QuizForm()
    return render(request, 'quiz_app/create_quiz.html', {'quiz_form': quiz_form})

def create_questions(request):
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question_form.save()
            return redirect('create_questions')
    else:
        question_form = QuestionForm()
    return render(request, 'quiz_app/create_questions.html', {'question_form': question_form})

def delete_quiz(request, pk):
    quiz = Quiz.objects.get(pk=1)
    quiz.delete()
    return redirect('/')
        