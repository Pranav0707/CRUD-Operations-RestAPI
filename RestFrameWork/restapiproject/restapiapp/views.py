from asyncio import Task
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from restapiapp.models import Tasks
from restapiapp.serializers import TasksSerializer


# Create your views here.
@api_view(['GET'])
def index(request):
    api_urls={
        'LIST':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def tasklist(request):
    tasks=Tasks.objects.all()
    serializer=TasksSerializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskdetail(request,pk):
    tasks=Tasks.objects.get(id=pk)
    serializer=TasksSerializer(tasks,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskcreate(request):
    serializer=TasksSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskupdate(request,pk):
    tasks=Tasks.objects.get(id=pk)
    serializer=TasksSerializer(instance=tasks,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def taskdelete(request,pk):
    tasks=Tasks.objects.get(id=pk)
    tasks.delete()

    return Response()
