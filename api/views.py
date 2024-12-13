from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
class PostView(ListView):
  model = Post

class PostCreateView(CreateView):
  model = Post
  fields = ["title"]
  success_url = reverse_lazy("posts")

class PostUpdateView(UpdateView):
  model = Post
  fields = ["title"]
  success_url = reverse_lazy("posts")

class PostDeleteView(DeleteView):
  model = Post
  success_url = reverse_lazy("posts")