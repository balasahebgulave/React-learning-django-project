from django.shortcuts import render
from . models import Todo
from . serializers import TodoSerializer
from rest_framework import viewsets


class TodoViewset(viewsets.ModelViewSet):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer


