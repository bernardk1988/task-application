from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages

from django.shortcuts import redirect,render,get_object_or_404

from .serializers import TodoSerializer
from .models import Todo

@api_view(["get"])
def todo_api(request):
    todos = Todo.objects.all().order_by("-id")
    serializer = TodoSerializer(todos,many=True)
    return Response({"success":True,
                    "message":"All todo data retrieved successfully",
                    "data":serializer.data},status=status.HTTP_200_OK)
def todo_list(request):
    todos = Todo.objects.all().order_by('-id')
    return render(request,'todo/todo_list.html',{"todos":todos})
@api_view(["POST"])
def add_todo_api(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
         todo=serializer.save()
         return Response({
            "success":True,
            "message": "Response:Task added successfully!",
            "data":TodoSerializer(todo).data,
        }, status=status.HTTP_201_CREATED)
 
    return Response({
         "success":False,
         "message": "Task not added",
         "errors": serializer.errors
     }, status=status.HTTP_400_BAD_REQUEST)
def add_todo(request):
    if request.method == "POST":
        serializer = TodoSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            messages.success(request, "Task added successfully!")
        else:
            messages.error(request, str(serializer.errors))
    return redirect("todo_list")

@api_view(["POST","PUT","PATCH"])
def update_todo_api(request,pk):
    todo = get_object_or_404(Todo,pk=pk)
    serializer = TodoSerializer(todo,data=request.data,partial = (request.method in ["PATCH", "POST"]))
    if serializer.is_valid():
        serializer.save()
        return Response({
            "success":True,
            "message":f"Response: Task {request.method} updated successfully!",
            "data": serializer.data,
        },status=status.HTTP_200_OK)
    return Response({
        "success":False,
        "message":"Task not updated",
        "errors": serializer.errors,
    },status=status.HTTP_400_BAD_REQUEST)
def edit_todo(request,pk):
    todo=get_object_or_404(Todo,pk=pk)
    if request.method == "POST":
        todo.task = request.POST.get("task")
        todo.datetime = request.POST.get("datetime")
        todo.status = request.POST.get("status")
        todo.save()
        messages.success(request,"Task Updated successfully")
        return redirect('todo_list')
    todos = Todo.objects.all().order_by("-id")

    return render(request, "todo/todo_list.html", {
        "todos": todos,
        "edit_todo": todo,
    })

@api_view(["POST","DELETE"])
def delete_todo_api(request, pk):

    todo = get_object_or_404(Todo, pk=pk)

    todo.delete()

    return Response({
        "success": True,
        "message": "Response Message Task deleted successfully!"
    }, status=status.HTTP_200_OK)