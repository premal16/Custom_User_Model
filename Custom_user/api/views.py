from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth import login
from .models import CustomUser
from .serializers import CustomUserSerializer,UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CustomUserSerializer


# @csrf_exempt

# @method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        print(user)
        if user :
            login(request, user)
            refresh = RefreshToken.for_user(user)
            data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            }
            return Response(data, status=200)
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserProfile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user 
        return Response({'username': user.username, 'email': user.email})