from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django import template
from blog.models import  Post
# Create your views here.

def home(request):
    user = {"name" : "Kevin"}

    return(render_to_response("home.html", locals()))
    #return (HttpResponse("success!"))

def portrait(request):
    return (render_to_response("fullframe.html", locals()))

def fullframe(request):
    return (render_to_response("fullframe.html", locals()))

def mediumformat(request):
    return (render_to_response("mediumformat.html", locals()))

def lifestyle(request):
    return (render_to_response("lifestyle.html", locals()))

def travel(request):
    return (render_to_response("travel.html", locals()))

def link(request):
    return (render_to_response("link.html", locals()))

def aboutme(request):
    return (render_to_response("aboutme.html", locals()))

def blog(request):
    posts = Post.objects.all()
    return (render_to_response("blog.html", locals()))

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post_detail.html', {'post': post})

