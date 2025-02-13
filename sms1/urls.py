from django.urls import path

from .views import add,success,register,user_login,user_logout,home

urlpatterns = [
    path('',home, name='home'),
    path('add/',add,name='add_school'),
    path('success/',success,name='success'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]