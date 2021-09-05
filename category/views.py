# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def index(request):
    return Response({'message': 'Index Function'})

@api_view(['GET'])
def show(request, id):
    return Response({'message': "Show function will get values from url"})


@api_view(['GET'])
def search(request):
    print(request.query_params)
    return Response({'message': f'Search function will get values from querystring {request.query_params}' })
