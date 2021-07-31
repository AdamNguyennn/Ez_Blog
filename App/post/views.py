from django.shortcuts import render
from .models import List
# Create your views here.
def index(request):
	list_post = List.objects.all()
	return render(request, 'index.html', {'lists':list_post})

def post(request, pk):
	list_post = List.objects.get(id=pk)
	return render(request, 'post.html', {'lists':list_post})