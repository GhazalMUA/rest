from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer , CardioSerializer
from .models import Cardio
from rest_framework import status

class UserRegisterView(APIView):
    def post(self,request):
        serialized_data = UserRegisterSerializer(data=request.POST)
        if serialized_data.is_valid():
            User.objects.create_user(username=serialized_data.validated_data['username'] , email=serialized_data.validated_data['email'] , password=serialized_data.validated_data['password'])
            return Response (serialized_data.data , status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors , status=status.HTTP_400_BAD_REQUEST)
    
    
    
class CardioView(APIView):
    def get(self,request):
        cardios=Cardio.objects.all()
        serialized_items=CardioSerializer(instance=cardios , many=True)
        return Response(data=serialized_items.data)
        
    def post(self,request):    
        serialized_item=CardioSerializer(data=request.POST)
        if serialized_item.is_valid():
           Cardio.objects.create(sport_name=serialized_item.validated_data['sport_name'] , callory_burning=serialized_item.validated_data['callory_burning'], coach=serialized_item.validated_data['coach'])
           return Response(data=serialized_item.data) 
        return Response ({'error':'your input data was wrong'})