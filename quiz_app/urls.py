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
    path('my_questions/', views.my_questions, name='my_questions'),
    path('edit_question/<int:pk>', views.edit_question, name='edit_question')

]