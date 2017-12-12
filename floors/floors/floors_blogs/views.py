from django.shortcuts import render
from django.views.generic import ListView, DetailView
from floors.floors_blogs.models import Post

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post
