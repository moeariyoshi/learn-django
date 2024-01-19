from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Post

def index(request):
    latest_posts = Post.objects.order_by('-pub_date')[:5]
    context = {'latest_posts': latest_posts}
    return render(request, 'myapp/index.html', context)
