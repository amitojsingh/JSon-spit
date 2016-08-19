from django.shortcuts import render
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

class ProductList(APIView):
	def get(self,request):
		datas=Product.objects.filter( id='1')
		print datas
		serializer=ProductSerializer(datas,many=True)
#		json_data = serializers.serialize('json', data)
		return Response(serializer.data)
