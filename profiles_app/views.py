from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_app import serializers



class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})


    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            city_name = serializer.validated_data.get('city_name')
            message = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&Appid=458449704162ef73cbf18469dc290e17'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
