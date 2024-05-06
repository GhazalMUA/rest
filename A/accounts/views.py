from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer

class UserRegisterView(APIView):
    def post(self,request):
        serialized_data = UserRegisterSerializer(data=request.POST)
        if serialized_data.is_valid():
            User.objects.create_user(username=serialized_data.validated_data['username'] , email=serialized_data.validated_data['email'] , password=serialized_data.validated_data['password'])
            return Response (serialized_data.data)
        return Response(serialized_data.errors)