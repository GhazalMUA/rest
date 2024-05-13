from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer , UserSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

class UserRegisterView(APIView):
    def post(self,request):
        serialized_data = UserRegisterSerializer(data=request.POST)
        if serialized_data.is_valid():
            User.objects.create_user(username=serialized_data.validated_data['username'] , email=serialized_data.validated_data['email'] , password=serialized_data.validated_data['password'])
            return Response (serialized_data.data , status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors , status=status.HTTP_400_BAD_REQUEST)
    
    
class UserViewset(viewsets.ViewSet): 
    
    permission_classes =[IsAuthenticated]
    queryset = User.objects.all()
    
    def list(self, request):
        serialized_data = UserSerializer(instance=self.queryset , many=True)
        result=data=serialized_data.data
        print(result)
        return Response(data=serialized_data.data)

    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset , pk=pk)
        serialized_item = UserSerializer(instance=item )
        return Response(data=serialized_item.data)


    def partial_update(self, request, pk=None):
        user = get_object_or_404(self.queryset , pk=pk)
        if user != request.user:
            return Response ({'permission denied':'you dont have such permission'})
        serialized_data= UserSerializer(instance=user  , data=request.POST , partial=True)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response (data=serialized_data.data)
        return Response (data=serialized_data.errors)


    def destroy(self, request, pk=None):
        user=get_object_or_404(self.queryset , pk=pk)
        if user != request.user:
            return Response({'permission denied':'error:you dont have this permission'})
        user.is_active = False
        user.save()
        return Response({'message':'user deactivated.'})  
        
 