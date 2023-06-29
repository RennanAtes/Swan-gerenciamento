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
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if not username or not password or not email:
        return Response({'message': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

    # Verificar se o usuário ou o e-mail já existem
    existing_user = User.objects.filter(username__iexact=username).first()
    if existing_user:
        return Response({'message': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
    
    existing_email = User.objects.filter(email__iexact=email).first()
    if existing_email:
        return Response({'message': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

    # Criar o novo usuário
    user = User.objects.create_user(username=username, password=password, email=email)
    
    return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)




@api_view(['POST'])
def user_login(request):

    
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        user_data = {
            'username': user.username,
            'email': user.email,
            # Adicione outros campos do usuário que você deseja retornar
        }
        
        
        return Response({
            'message': 'Login successful',
            'access_token': access_token,
            'refresh_token': refresh_token,
            'user': user_data,
        }, status=200)
    else:
        return Response({'message': 'Invalid credentials'}, status=401)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    
    try:
        # Captura o token de acesso do cabeçalho de autorização
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        access_token = auth_header.split('Bearer ')[1]

        
        
        # Invalida o token de acesso para fazer logout
        try:
            token = OutstandingToken.objects.get(token=access_token)
            token.blacklisted = True
            token.save()
        except OutstandingToken.DoesNotExist:
            pass
        
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
    except Exception as e:
        
        
        
        return Response({'message': 'Error during logout'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def todos_usuarios(request):

    user = request.user
    access_token = AccessToken.for_user(request.user)
    
    




    usuarios = User.objects.all()
    user_data = [{'id': user.id, 'username': user.username} for user in usuarios]
    return Response({'Usuarios': user_data}, status=status.HTTP_200_OK)
