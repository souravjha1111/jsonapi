from rest_framework import viewsets, status
from .models import blogData
from .serializers import blogDataSeriallizer
from rest_framework.response import Response
# from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.cache import never_cache

# userlist method to view all users at once with options as get and post

@api_view(['GET'])
@never_cache
def get_all_data(request):
    if request.method == 'GET':    
        data = blogData.objects.all()
        serializer = blogDataSeriallizer(data,many = True)
        return Response(serializer.data)



@api_view(['GET'])
@never_cache
def get_data(request, id):
    data = blogData.objects.get(pk=id)
    if request.method == 'GET':
        serializer = blogDataSeriallizer(data)
        return Response(serializer.data)


@api_view(['POST'])
@never_cache
def post_data(request):
    if request.method == 'POST':
        serializer = blogDataSeriallizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['DELETE', 'GET'])
@never_cache
def delete_data(request,id):
    data = blogData.objects.get(pk=id)
    if request.method == 'DELETE' or request.method == 'GET':
        data.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)