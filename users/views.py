from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EmployeeSerializer
from .models import Employee
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all().order_by('-id')
    serializer_class=EmployeeSerializer
