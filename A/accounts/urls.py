from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_token
from rest_framework import routers
from .views import UserViewset

app_name='accounts'
urlpatterns=[
    path('user_register/' , views.UserRegisterView.as_view() ,name='user_register') ,
    path('api-token-auth/', auth_token.obtain_auth_token),

]

router = routers.SimpleRouter()
router.register('users', UserViewset)
urlpatterns += router.urls

