from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from .serializer import *
from .models import *

# Create your views here.



#@api_view(["GET","PUT","DELETE","POST"])
class people_list(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class= PersonSerializer




  
