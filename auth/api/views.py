# Rest Framework imports
from tokenize import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.request import Request
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# project import
from .serializer import RegisterSerializer, CustomAuthTokenSerializer


def success_response(data, message, status_code=200, send_data=True):
    response = {
        'success': True,
        'message': message,
    }
    if send_data:
        response['data'] = data
    return Response(response, status=status_code)


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = CustomAuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            print(user, 'user')
            data = {
                'token': token.key,
                'user_id': user.pk,
                'email': user.email,
                'username': user.username,  # Include the username
            }

            return success_response(data, 'Sucessfully logged in')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def LogoutViewSet(request):
    if request.method == 'POST' and request.user.is_authenticated:
        request.auth.delete()
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Not authenticated or already logged out'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST', ])
def RegistrationViewSet(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = "Register successfully"
            data['username'] = account.username
            data['email'] = account.email

            return success_response(data, message='Successfully Registered')

        else:
            data = serializer.errors
    return Response(data)


__all__ = [
    'LogoutViewSet', 'RegistrationViewSet', 'CustomAuthToken'
]
