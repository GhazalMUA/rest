from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer , CardioSerializer , QuestionSerializer , AnswerSerializer
from .models import Cardio , Question , Answer
from rest_framework.permissions import IsAdminUser , IsAuthenticated
from rest_framework import status
from permissions import IsOwnerOrReadOnly
# Create your views here.

class HomeView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        persons=Person.objects.all()
        serialized_data = PersonSerializer(instance=persons , many=True)
        return Response(data=serialized_data.data)
    

   
class CardioView(APIView):
    def get(self,request):
        cardios=Cardio.objects.all()
        serialized_items=CardioSerializer(instance=cardios , many=True)
        return Response(data=serialized_items.data)
        
    def post(self,request):    
        serialized_item=CardioSerializer(data=request.data)
        if serialized_item.is_valid():
           Cardio.objects.create(sport_name=serialized_item.validated_data['sport_name'] , callory_burning=serialized_item.validated_data['callory_burning'], coach=serialized_item.validated_data['coach'])
           return Response(data=serialized_item.data) 
        return Response ({'error':'your input data was wrong'})
    
    
class QuestionListView(APIView):
    def get(self,request):
        questions= Question.objects.all()
        serialized_data= QuestionSerializer(instance=questions , many=True).data
        return Response(serialized_data , status=status.HTTP_200_OK)
    
    
class QuestionCreateView(APIView): 
    permission_classes=[IsAuthenticated]  
    def post(self,request , *args, **kwargs):
        print(request.data)
        serialized_data = QuestionSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data , status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class QuestionUpdateView(APIView):    
    permission_classes=[IsOwnerOrReadOnly]
    def put(self,request,pk):
        question=Question.objects.get(pk=pk)
        self.check_object_permissions(request,question)
        ser_data=QuestionSerializer(instance=question, data=request.data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data , status=status.HTTP_200_OK)
        return Response(ser_data.errors , status=status.HTTP_400_BAD_REQUEST)
        
    
class QuestionDeleteView(APIView):    
    def delete(self,request,pk):
        question=Question.objects.get(pk=pk)
        question.delete()
        return Response({'message':'question deleted'}, status=status.HTTP_200_OK)