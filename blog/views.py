from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q

from blog.models import Post


class ListObjectsView(ListView):
    model = Post
    template_name = "main.html"
    context_object_name = "posts"


class DetailObjectsView(DetailView):
    model = Post
    template_name = "detail.html"
    context_object_name = 'post'


class SearchResaultsView(ListView):
    model = Post
    template_name = "search_results.html"
    context_object_name = 'post'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(Q(title__icontains=query))
        return object_list


class NeedUpdateView(UpdateView):
    model = Post
    template_name = "edit.html"
    fields = 'title', 'desc'
    success_url = '/'


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'
    template_name = "delete.html"


class PostCreateView(CreateView):
    model = Post
    fields = 'author', 'image', 'title', 'desc'
    template_name = "create.html"
    success_url = '/'