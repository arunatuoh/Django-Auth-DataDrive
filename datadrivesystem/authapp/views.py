from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework import authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserSerializer
from django.contrib.auth import get_user_model


@csrf_exempt
class UserRegistrationAPI(APIView):
    """
    Allows users to register by providing their email and password.
    Successful registration returns user details and a success message.
    Invalid input returns error details and a bad request status.
    """
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)

        if serializer.is_valid():
            # Get the user model (Custom User model)
            User = get_user_model()
            # Hash the user's password using Django's default password hashing
            password = serializer.validated_data['password']
            user = User.objects.create_user(
                email=serializer.validated_data['email'],
                password=password
            )
            response_data = {
                'message': 'User registered successfully',
                'user_id': user.id,
                'email': user.email,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# In views.py of authapp
@csrf_exempt
class UserLoginAPI(APIView):
    """
    Allows users to log in by providing their email and password.
    Successful login returns a success message.
    Invalid credentials return an error message and unauthorized status.
    """
    authentication_classes = [authentication.BasicAuthentication]
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)