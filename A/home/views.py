from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer
# Create your views here.
class HomeView(APIView):
    def get(self,request):
        persons=Person.objects.all()
        serialized_data = PersonSerializer(instance=persons , many=True)
        return Response(data=serialized_data.data)
    

