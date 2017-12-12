from django.conf.urls import url
from django.urls import path
from floors.floors_blogs.views import PostListView, PostDetailView
from floors.floors_blogs.models import Post

urlpatterns = [
    path('',PostListView.as_view(), name = 'list'),
    path(str(Post.get_url(Post)), PostDetailView.as_view())
]

