from django.urls import path
from . import views as accountView

urlpatterns = [
    path('',accountView.home,name='accountHome'),
    path('/signup/',accountView.signup,name='signup'),
    path('/login/',accountView.login,name='login'),
]
