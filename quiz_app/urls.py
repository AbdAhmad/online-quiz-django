from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('quizes/', views.quizes, name='quizes'),
    path('quiz/<int:id>/', views.quiz, name='quiz'),
    path('create_quiz/', views.create_quiz, name='create_quiz'),
    path('create_question/', views.create_question, name='create_question'),
    path('my_quizes', views.my_quizes, name='my_quizes'),
    path('profile/', views.profile_page, name='profile'),
    path('edit_profile/<int:pk>', views.edit_profile, name='edit_profile'),
    path('edit_quiz/<int:pk>', views.edit_quiz, name='edit_quiz'),
    path('delete_quiz/<int:pk>/', views.delete_quiz, name='delete_quiz'),
    path('quiz_questions/<int:pk>/', views.quiz_questions, name='quiz_questions'),
    path('edit_question/<int:pk>/', views.edit_question, name='edit_question'),
    path('delete_question/<int:pk>/', views.delete_question, name='delete_question'),
    path('author_profile/<str:username>', views.author_profile, name='author_profile'),
    path('author_quizes/<str:username>', views.author_quizes, name='author_quizes'),
    path('search_quiz/', views.search_quiz, name='search_quiz'),
    path('save_ans/', views.save_ans, name='save_ans'),
    path('result/', views.result, name='result')
]