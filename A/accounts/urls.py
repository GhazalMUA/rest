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

