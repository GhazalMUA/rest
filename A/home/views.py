from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer , CardioSerializer , QuestionSerializer , AnswerSerializer
from .models import Cardio , Question , Answer
from rest_framework.permissions import  IsAuthenticated
from rest_framework import status
from permissions import IsOwnerOrReadOnly
from django.core.paginator import Paginator
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
    

    
    
##############################################pagination###################################################    
    
# I want to add pagination. there are two ways. first when you want to add pagination to all your views you can change the seetings of your project.
# # REST_FRAMEWORK = {
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
#     'PAGE_SIZE': 100
# }
#you can change your page size and customize it. but it will apply to all type of views exept APIVIEW and VIEWSETS.
#f you want to pply pagination to a specific view, forexample here to my lists of questions. first import paginator.
#and then you have two type of conditions
class QuestionListView(APIView):
    def get(self,request):
        questions= Question.objects.all()
        page_number= self.request.query_params.get('page',1)        # age az tarighe url shomare safe ferestade bod begiresh dar gheyre in sorat bezaresh 1
        page_Size=self.request.query_params.get('limit' , 2  )
        paginator=Paginator(questions,page_Size, )   #ye moteghater misazam be esme paginator ya hala har esmi k mikhaym bhsh midim va az kelase Paginator ke bala import shode instance misazim. in kelas chandta vorodi mikhad. yekish ine ke mikhay chi ro ghete ghete koni? migim questions ro ke darvaghe too delesh hameye soalato dare. hala arguman baadi mige har ghete at mikhat cheghadri bashe ke mishe page_size
        serialized_data= QuestionSerializer(instance=paginator.page(page_number) , many=True).data     #dige inja tooye instance , nemiaym questions ro bezarim bejash paginator ro gharar midim. in kelase paginator age beri too mostanadatesh ye method dare be esme page ke in methode e oage ye vorodi migire ke shomarer safe ast ke inja ma tahte onvane page_number taarifesh kardim.
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