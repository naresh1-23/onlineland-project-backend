from django.shortcuts import render
from .models import Post
from rest_framework.response import Response
from .serializers import PostSerializer
from rest_framework.decorators import api_view

@api_view(['POST'])
def postdata(request):
    try:
        data = request.data
        serializer = PostSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'Status': 200,
                "message": "Successfully added",
            })
        else:
            return Response({
                "Status" : 400,
                "Message": "Invalid data"
            })
    except Exception as e:
        return Response({
            "Status": 500,
            "Message":"Server Error. Please Try again."
        })
        
@api_view(['GET'])
def getdata(request):
    data = Post.objects.all()
    serializer = PostSerializer(data, many = True)
    return Response({
        "Status":200,
        "Message": "Data successfully retrieved",
        'data': serializer.data
    })
    
@api_view(['GET'])
def getsingledata(request, pk):
    data = Post.objects.get(id = pk)
    serializer = PostSerializer(data = data)
    return Response({
        "Status":200,
        "Message":"Data retrieved",
        "data": serializer.data
    })
    
    