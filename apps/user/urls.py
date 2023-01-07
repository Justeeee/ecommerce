from django.urls import path
from apps.user.views import UserCreateApiView, UserLoginView, UserLogOutView

urlpatterns = [

    path('register/', UserCreateApiView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogOutView.as_view(), name='logout'),
]
