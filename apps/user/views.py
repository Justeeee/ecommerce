from django.contrib.auth import authenticate, login, logout
from apps.user.models import User
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from apps.user.serializers import UserCreateModelSerializer, LoginSerializer
# from user.serializers import LogOutSerializer


class UserCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateModelSerializer


class UserLoginView(RetrieveAPIView):
    serializer_class = LoginSerializer
    queryset = User.objects.all()

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            data = {
                'message': 'zor'
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# class UserLogOutView(RetrieveAPIView):
#     serializer_class = LogOutSerializer
#     queryset = User.objects.all()
#
#     def post(self, request):
#         if request.user.is_authenticated:
#             logout(request)
#             data = {'success': 'Sucessfully logged out'}
#             return Response(data=data, status=status.HTTP_200_OK)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)