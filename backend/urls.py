from django.urls import path
from .views import *
urlpatterns = [
    path('login',loginHandler,name="login"),
    path('signup',register,name="signup"),
    path('',mainForm,name='homepage'),
    path('logout',logoutHandler,name="logout"),
]
