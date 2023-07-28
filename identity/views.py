from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from identity import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
# Create your views here.

'''
User Create API View
'''
class UserCreateAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class =serializers.CreateuserSerializer

'''User Login '''
class UserloginViewset(ObtainAuthToken, APIView):
     serializer_class =  serializers.AuthtokenSerializer
     permission_classes = (AllowAny,)
     renderer_classes= api_settings.DEFAULT_RENDERER_CLASSES

     def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'Message':'Login Successfully',
            'token': token.key,
            
            'user details':{
            'user_id': user.pk,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'user_profile':user.user_profile,
            'created_at': user.created_at
        }})
        