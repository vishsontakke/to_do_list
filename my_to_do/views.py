from django.shortcuts import render
from .models import Todolist
from rest_framework.response import Response
from rest_framework import status
from .serilizers import TodolistSerilizer
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view

# def testview(request):
#     tasks = Todolist.objects.all()
#     serializer = TodolistSerilizer(tasks, many=True)  
#     print(serializer.data)  
#     return JsonResponse(serializer.data, safe=False)

class TodoListApis(viewsets.ModelViewSet):
    queryset = Todolist.objects.all()
    serializer_class = TodolistSerilizer 
   

@api_view(['GET'])
def completed_tasks(request):
    todos = Todolist.objects.filter(is_completed= True)
    serlizer= TodolistSerilizer(todos,many=True)
    return Response(serlizer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_task(request, task_id):
    try:
        task = Todolist.objects.get(id=task_id)
        task.delete()
        return Response({"message": "Task deleted successfully."}, status=status.HTTP_200_OK)
    except Todolist.DoesNotExist:
        return Response({"error": "Task not found."}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT'])
def update_task(request, task_id):
    try:
        task = Todolist.objects.get(id=task_id)
    except Todolist.DoesNotExist:
        return Response({"error": "Task not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = TodolistSerilizer(task, data=request.data, partial=True)  
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)