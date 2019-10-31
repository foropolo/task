from profiles_app import serializers
from django.core.management.base import BaseCommand
from rest_framework.response import Response
from rest_framework import serializers


import urllib.request
import json
import urllib


class TakeJsonData():
    """Take name city and give back weather data"""
    city_name = serializers.CharField(max_length=200)

    def TakeCityGiveWeather(self,request):
        return ""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            city_name = serializer.validated_data.get('city_name')
            #url = "http://api.openweathermap.org/data/2.5/weather?q=%s&Appid=458449704162ef73cbf18469dc290e17" % (city_name,)
            url = '{}{}{}'.format('http://api.openweathermap.org/data/2.5/weather?q=',city_name,'&Appid=458449704162ef73cbf18469dc290e17')
            response = urllib.request.urlopen(url)
            dataforo = json.loads(response.read())
            temperature = dataforo.get("main")
            return temperature
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
