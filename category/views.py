# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def index(request):
    return Response({'message': 'Index Function'})

@api_view(['GET'])
def show(request):
    return Response({'message': request.query_params})
