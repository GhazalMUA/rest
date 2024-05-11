from django.urls import path
from . import views

app_name='home'
urlpatterns = [
    path('' , views.HomeView.as_view() , name= 'home'),
    path('cardio/' , views.CardioView.as_view() , name='cardio'),
    path('questions/' , views.QuestionListView.as_view(), name='questions'),
    path('question/create/' , views.QuestionCreateView.as_view(), name='question'),
    path('question/update/<int:pk>/' , views.QuestionUpdateView.as_view(), name='question'),
    path('question/delete/<int:pk>/' , views.QuestionDeleteView.as_view(), name='question'),
]