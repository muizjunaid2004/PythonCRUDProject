from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TaskSerializer
from .models import Task
# Create your views here.

#Brief overview of all routes
@api_view(['GET'])
def overview(request):
    urls = {
        'Delete': '/task-delete/<str:pk>',
        'Update': '/task-delete/<str:pk>',
        'Create': '/task-create/<str:pk>',
        'List': '/task-list/', 
        'Detail': '/task-detail/<str:pk>'
    }
    return Response(urls)

#Creating tasks
@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#Updating specific task
@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#Updating specific task
@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Item deleted")


@api_view(['GET'])

#Listing tasks
def taskList(request):
    tasks = Task.objects.all()
    #Pass in many if serializing many objects
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

#Detail of specific task
@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)




