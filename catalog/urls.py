from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('products',views.ProductList.as_view()),
    path('api_view',views.api_view,name='api_view'),
    
]
