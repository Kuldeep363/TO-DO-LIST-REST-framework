from django.urls import path
from . import views as accountView

urlpatterns = [
    path('',accountView.home,name='accountHome'),
    path('signup/',accountView.signup,name='signup'),
    path('login/',accountView.loginS,name='login'),
    path('userApi',accountView.userS,name='signupApi'),
    path('signupApi',accountView.signupS,name='signupApi'),
    path('logout',accountView.logoutS,name='logout'),
]
