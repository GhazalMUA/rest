from rest_framework import serializers
from .models import Cardio , Question , Answer
class PersonSerializer(serializers.Serializer):
    name=serializers.CharField()
    age=serializers.IntegerField()
    email=serializers.EmailField()
    
    
    
class CardioSerializer(serializers.ModelSerializer):
    date=serializers.CharField()
    class Meta:
        
        model = Cardio
        fields = ('sport_name' , 'callory_burning','coach' , 'date')      #if you want to choose one or multiple item just like forms you should assign them in a tople
    
    def validate_coach(self,value):
        if value == 'admin':
            raise serializers.ValidationError('coach name shouldnt be admin')
        return value    
    
    
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
        
        
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'