from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('quizes/', views.quizes, name='quizes'),
    path('quiz/<int:id>/', views.quiz, name='quiz'),
    path('create_quiz/', views.create_quiz, name='create_quiz'),
    path('create_questions/', views.create_questions, name='create_questions'),
    path('delete_quiz/<int:id>', views.delete_quiz, name='delete_quiz')
]