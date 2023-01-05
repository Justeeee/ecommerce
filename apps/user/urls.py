from django.urls import path
from apps.user.views import UserCreateApiView, GetMeApiView, LoginView

urlpatterns = [

    path('register/', UserCreateApiView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('get-me/', GetMeApiView.as_view(), name='get_me'),

]
