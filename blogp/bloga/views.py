from django.views import generic
from .models import Post
from django.shortcuts import render
from django.views.generic import TemplateView
from . import views

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog1.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class MainPageView(TemplateView):
    template_name ='indexing.html'