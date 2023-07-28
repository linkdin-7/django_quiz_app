# Importing Required Libraries
from .models import User
from rest_framework import serializers
from django.core import exceptions
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model,authenticate , password_validation
from django.core.validators import validate_email
from django.contrib.auth.hashers import make_password

#Overriding a default User Create Serializer
class CreateuserSerializer(serializers.ModelSerializer):
      
    password= serializers.CharField(write_only=True,min_length=8,required=True)
    confirm_password= serializers.CharField(write_only=True,min_length=8,required=True)
    def validate(self, attrs):
        
        try:
            if User.objects.filter(email= attrs['email']).exists():
                raise serializers.ValidationError('This Email is Already Used')
            
            if attrs['password'] != attrs['confirm_password']:
                raise serializers.ValidationError('This Password Not Match')

            else: 
                password_validation.validate_password(attrs['password'])  
                validate_email(attrs['email'])
              
        except exceptions.ValidationError as exc:
            raise serializers.ValidationError(str(exc))
        return attrs
    class Meta:
        model=User
        fields = [
        'id','email','first_name','last_name','password','confirm_password','user_profile','created_at']
        read_only_fields = ['id',]
    def create(self, validated_data):
     if validated_data.get('password') != validated_data.get('confirm_password'):
        raise serializers.ValidationError("Those password don't match") 

     elif validated_data.get('password') == validated_data.get('confirm_password'):
            validated_data['password'] = make_password(
                validated_data.get('password')
            )

     validated_data.pop('confirm_password') 
     return super(CreateuserSerializer, self).create(validated_data)


# Creating a Authentication by token Serializer
class AuthtokenSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField(
        style={
            'input_type':'password'

        }
    )
    
    def validate(self, attrs):
        email=attrs.get('email')
        password=attrs.get('password')

        user=authenticate(
            request=self.context.get('request'),
            email=email,
            password=password,


        )
        if not user:
            msg='unable to determine'
            raise serializers.ValidationError(msg,code='authentication')
        attrs['user']= user
        return attrs