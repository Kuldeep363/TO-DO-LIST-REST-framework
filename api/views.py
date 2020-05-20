from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
# from rest_framework.views import APIView # for class based views
# from rest_framework import status
# from rest_framework import generics # for mixins and generic based class views
# from rest_framework import mixins #for mixins based class views

from django.http import Http404
from .models import Tasks
from django.contrib.auth.models import User
from datetime import datetime as dt
# Create your views here.

@api_view(['GET'])
def apiUrls(request):
    api_urls={
        'To see the list of tasks':'http://127.0.0.1:8000/api/task-list',
        'To create new task':'http://127.0.0.1:8000/api/task-create',
        'To update a task':'http://127.0.0.1:8000/api/task-update/slug',
        'To delete a task':'http://127.0.0.1:8000/api/task-delete/slug',
    }

    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    user = request.user
    if user.is_authenticated:
        tasks = Tasks.objects.filter(taskOwner = user.username).order_by('-id')
        serializer = TaskSerializer(tasks,many=True)
        return Response(serializer.data)
    else:
        return Response({'error':'Authentication require! Please Signin'})

# @api_view(['GET'])
# def taskDetail(request,slug=None):
#     task = Tasks.objects.get(taskSlug = slug)
#     serializer = TaskSerializer(task,many=False)
#     return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    user = request.user
    if user.is_authenticated:
        data = request.data
        print(user.username)
        data['taskOwner'] = user.username
        data['taskSlug'] = dt.now().strftime('%H%M%Y%d%m%S')
        serializer = TaskSerializer(data = data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
    else:
        return Response({'error':"permission Denied"})

@api_view(['POST'])
def taskUpdate(request,slug=None):
    user = request.user
    if user.is_authenticated:
        task = get_object_or_404(Tasks,taskSlug = slug)
        if task.taskOwner == user.username:
            serialize = TaskSerializer(instance = task, data = request.data)

            if serialize.is_valid():
                serialize.save()
                return Response(serialize.data)
        else:
            return Response({'error':'Permission Denied'})        
    else:
        return Response({'error':'Permission Denied Authentication needed'})

@api_view(['DELETE'])
def taskDelete(request,slug = None):
    user = request.user
    if user.is_authenticated:
        task = get_object_or_404(Tasks,taskSlug = slug)
        if task.taskOwner == user.username:   
            task.delete()
            return Response('Task Delete Successfully!')
        else:
            return Response({'error':'Permission Denied! You are not owner of this task'})        
    else:
        return Response({'error':'Permission Denied'})




'''
    urls used for default class based views
'''

# class taskList(APIView):
#     def get(self,request,format = None):
#         task = Tasks.objects.all()
#         serializer = TaskSerializer(task,many = True)
#         return Response(serializer.data)

#     def post(self,request,format = None):
#         serializer = TaskSerializer(data = response.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         return Response(serializer.errors,status = status.HTTP_404_NOT_FOUND)

# taskList = taskList.as_view()


# class taskDetails(APIView):

#     def get_object(self,id):
#         try:
#             return Tasks.objects.get(id = id)
#         except Tasks.DoesNotExist:
#             raise Http404
    

#     def get(self,request,id,format = None):
#         task = Tasks.objects.get(id = id)
#         serializer = TaskSerializer(task,many = False)
#         return Response(serializer.data)

#     def put(self,request,id,format = None):
#         task = Tasks.objects.get(id = id)
#         serializer = TaskSerializer(task,data = request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#         return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

#     def delete(self,request,id,format = None):
#         task = Tasks.objects.get(id = id)
#         task.delete()
#         return Response('task deleted successfully!')

# taskDetail = taskDetails.as_view()



'''
    mixinx based class views
'''
# class taskList(mixins.ListModelMixin,
#                 mixins.CreateModelMixin,
#                 generics.GenericAPIView
#                 ):
#     queryset = Tasks.objects.all()
#     serializer_class = TaskSerializer
#     def get(self,request,*args, **kwargs):
#         return self.list(request,*args,**kwargs)

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)

# taskList = taskList.as_view()

# class taskDetails(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView
#                     ):
#     queryset = Tasks.objects.all()
#     serializer_class = TaskSerializer

#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)

#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)

#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)

# taskDetail = taskDetails.as_view()

'''
    generic based class views
'''
# class taskList(generics.ListCreateAPIView):
#     queryset = Tasks.objects.all()
#     serializer_class = TaskSerializer

# class taskDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Tasks.objects.all()
#     serializer_class = TaskSerializer

# taskList = taskList.as_view()
# taskDetail = taskDetails.as_view()