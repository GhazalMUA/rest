from django.urls import path
from . import views

app_name='accounts'
urlpatterns=[
    path('user_register/' , views.UserRegisterView.as_view() ,name='user_register') ,
]