from rest_framework import serializers
from django.contrib.auth.models import User


#third type of validation: you create a seperate function and work on that function. i mean its not a function of a class. its a seperate fnction. its good when you want to use a validator in many places. makesure to pass `value` to this function.
def clean_email(value):
    if 'admin' in value:
        raise serializers.ValidationError('you cant use `admin` in your email address')


class UserRegisterSerializer(serializers.Serializer):
    
    username=serializers.CharField(required=True)
    email=serializers.EmailField(required=True , validators=[clean_email])
    password=serializers.CharField(required=True , write_only=True)
    password2=serializers.CharField(required=True , write_only= True)
    
    
    #vthere are three type of validation for serializers:
    
    #FIELD LEVEL VALIDATION. you should write a function and the name of function begins with 'validat' and then a '_' and the name of that field you want to validate on. then pass 'self' as ever and 'value' to it. value is the meghadri ke karbar dare vase filed e username vared mikone.
    def validate_username(self,value):
        if value == 'admin':
            raise serializers.ValidationError('you cant choose`admin` for your username')
        return value
    
    
    #OBJECT LEVEL VALIDATION. you should overwrite `validate` method. here, `object` means the hole data which comes from user.
    def validate(self,data):     #data is the dictonary that all the input information which entered by user are in that.
        if data['password'] != data['password2']:
            raise serializers.ValidationError('passwords must match')
        
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'