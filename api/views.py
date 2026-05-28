from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import OvertimePost
from .serializers import OvertimePostSerializer
# Create your views here.
@api_view(['GET'])
def get_overtime(request): 
    posts = OvertimePost.objects.all()
    serializer = OvertimePostSerializer(posts, many = True)
    return Response(serializer.data)

