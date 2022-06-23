from pyexpat import model
from typing import Generic
from django.shortcuts import render
from django.views import generic
from .models import Post
from django.urls import reverse_lazy
# Create your views here.

class PostListView(generic.ListView):
    model = Post
    
class PostCreateView(generic.CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
    
class PostDetailView(generic.DeleteView):
    model = Post
    
class PostUpdateView(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")  
    
class PostDeleteView(generic.DeleteView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")   