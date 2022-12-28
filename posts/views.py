from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    return render(request, 'posts/home.html', {"posts": Post.objects.all() })
    
def detailPage(request, getid):
    return render(request, 'posts/details.html', {"post":Post.objects.get(id=getid)})

