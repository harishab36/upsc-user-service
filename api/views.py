from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UpscUser
from .serializers import UpscSerializer

# Create your views here.

@api_view(['GET'])
def homeApi(request):
    return Response('User Home')

@api_view(['POST'])
def crudUser(request):
    #create user
    print(request.data)
    user = UpscSerializer(data = request.data)
    if user.is_valid():
        user.save()
    return Response(user.data, status=201)

@api_view(['GET'])
def findUser(request, id):

    print(f"method {request.method} \n data: {id}")
    #Get user
    user = UpscSerializer(UpscUser.objects.get(userId=id),many = False)
    return Response(user.data)

@api_view(['GET'])
def findAllUsers(request):
    user = UpscUser.objects.all()
    usersSerialized = UpscSerializer(user, many=True)
    return Response(usersSerialized.data)