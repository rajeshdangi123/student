from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.renderers import JSONRenderer
from .serializers import SchoolSerializers,StudentSerializers
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
#from rest_framework.relations import ForeignKey

from app1.models import School,Student

# def home(request):
#     return HttpResponse("hello")

# Create your views here.

class SchoolViewSet(viewsets.ModelViewSet):
    queryset=School.objects.all()
    
    serializer_class=SchoolSerializers

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    
    serializer_class=StudentSerializers

class  SchoolData(APIView):
    def get(request,self ):
        pi =School.objects.all().values()
        return JsonResponse(list(pi),safe=False)
    
    
    
class StudentDAta(APIView):
    def get(request,self):
        pi=Student.objects.all().values()
        return JsonResponse(list(pi), safe=False )