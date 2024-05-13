from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_token
from rest_framework import routers
from .views import UserViewset
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
app_name='accounts'
urlpatterns=[
#     path('user_register/' , views.UserRegisterView.as_view() ,name='user_register') ,              in mored va morede paini vaseye default authentication token e django bodfan hala k darim az jwt estefade mikonim dg be ina niazi nadarim
#     path('api-token-auth/', auth_token.obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
 ]

router = routers.SimpleRouter()
router.register('users', UserViewset)
urlpatterns += router.urls

# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNTU4Njg4MSwiaWF0IjoxNzE1NTAwNDgxLCJqdGkiOiI4YWUyNzE5ZjgxMmM0YzQ0OWJlN2RhOGQ0OTJlNTFiMSIsInVzZXJfaWQiOjN9.oZ8A9aQtmb0NgxP1G0tZh5_41rWgJcrPjQtGQZ1mgOw",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1NTAwNzgxLCJpYXQiOjE3MTU1MDA0ODEsImp0aSI6IjQyZjFiNmQxOWQyNjRiMjA4YjdhMDcyZTY5OTU4M2RhIiwidXNlcl9pZCI6M30._3EKzQgzCMgolNe3B-08jj36f0c-cjRzqcbkABHopxU"
# }