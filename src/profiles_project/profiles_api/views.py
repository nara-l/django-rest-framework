from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class HelloApiView(APIView):
    """Test API View."""
    def get(self, request, format=None):
        """Returns a list of APIView features."""
        an_api_view = [
            'Uses HTTP methods as functions get, post, put, patch, delete',
            'It is similar to a traditional Django View',
            'Gives you the most control over your object',
            'Is mapped manually to your URLs'
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_api_view})
