from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UpscUser
from .serializers import UpscSerializer

# Create your views here.

@api_view(['GET'])
def homeApi(request):
    return Response('User Home')

@api_view(['POST','PUT'])
def crudUser(request):
    match request.method:
        case 'POST':
            #create user
            print(f"method {request.method} \n data: {request.path}")
            user = UpscSerializer(data = request.data)
            if user.is_valid():
                user.save()
            return Response(user.data, status=201)
        case 'PUT':
            #update
            return Response(status=201)            

def findOrDelete(request, id):
    match request.method:
        case 'GET':    
            #Get user
            user = UpscUser.objects.get(userId=id)
            user = UpscSerializer(user)
            return Response(user.data, status=200)
        case 'DELETE':
            return Response(status=201)