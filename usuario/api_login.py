from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.request import Request
from .tokens import create_jwt_pair_for_user



class ObterToken(APIView):

    def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404
            
    def post(self, request:Request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            # tokens = create_jwt_pair_for_user(user)
            user_name = self.get_user(username)
            response = {
                'message': "Login sucesso", 
                # 'tokens': tokens,
                
                'user': {
                    'id': str(user_name.id), 
                    'username': str(user_name), 
                    'email': str(user_name.email)
                }
                
                
            }
            return Response(data=response, status=status.HTTP_200_OK)

        else:
            return Response(data={"message": "Usuário ou senha inválida."})
