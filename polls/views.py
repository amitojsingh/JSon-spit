from django.shortcuts import render

from django.http import HttpResponse
from polls.models import Product

def index(request):
	product=Product.data
    	return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.
#<html>
#{{data}}
#{{json_data}}
#{{% spit %}}
#</html>
