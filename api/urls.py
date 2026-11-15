from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeApi, name='home'),
    path('user', views.crudUser,name='user-operations'),
    path('user/<str:pk>', views.crudUser,name='find-user'),
]