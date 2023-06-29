from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.tokens import RefreshToken, OutstandingToken, BlacklistedToken, AccessToken, OutstandingToken
from rest_framework_simplejwt.authentication import JWTAuthentication



@api_view(['POST'])
def criarPagina(request):

    nome_pagina = request.data.get('nome_pagina')
    print(nome_pagina)
    
    return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
