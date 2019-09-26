from django.shortcuts import render
from . import models
from . serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import generics
import requests
from django.http import HttpResponse
# Create your views here.
class ProductList(generics.ListAPIView):
    queryset=models.Product.objects.all()
    serializer_class=ProductSerializer

def api_view(request):
    url="http://127.0.0.1:5000/products?format=json"
    response=requests.get(url)
    des=response.json()
    print(des)
    for des in des:
        named=des['name']
        print(named) 
    


    return HttpResponse("Result")
