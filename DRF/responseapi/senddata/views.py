from django.shortcuts import render

#custom imports
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Data
from . serializers import DataSerializer

class DataList(APIView):
	"""
	# GET returns all data in model, Data
	# POST creates new data in model, Data
	"""
	def get(self, request):
		Data1 = Data.objects.all()  # store all instances or objects
		serializer = DataSerializer(Data1, many=True) # convt to many JSON objects
		return Response(serializer.data) # return JSON
	
	def post(self, request):
		serializer = DataSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)