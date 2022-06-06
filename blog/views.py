from turtle import title
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Post
# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class CreatePost(CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ['title', 'author', 'body']
    success_url = reverse_lazy('home')

class UpdatePost(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'body']

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('home')