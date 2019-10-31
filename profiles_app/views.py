from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_app import serializers
from profiles_app import jsongetter
from django import template

import urllib
import json


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
        city_name = request.data.get('city_name')
        #url = "http://api.openweathermap.org/data/2.5/weather?q=%s&Appid=458449704162ef73cbf18469dc290e17" % (city_name,)
        url = '{}{}{}'.format('http://api.openweathermap.org/data/2.5/weather?q=',city_name,'&Appid=458449704162ef73cbf18469dc290e17')
        print(url)
        try:
            response = urllib.request.urlopen(url)
            data = json.loads(response.read())
            temperature_kelvin = data.get("main").get("temp")
            temperature_celcius = temperature_kelvin - 273.15
            result_weather= round(temperature_celcius,2)
            final_result = 'The temperature of '+city_name+' is ' + str(result_weather)
            return Response(final_result)
        except urllib.error.URLError as e:
            return Response('This city does not exist in our database or the name is invalid .Try another one')

        #    return Response({'message': 'Type a valid city name'})
