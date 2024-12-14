from django.http import HttpResponse
from django import forms
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from api.forms import SignInForm, SignUpForm
from .models import Post
from django.contrib.auth.models import User

# Create your views here.
class PostView(ListView):
  model = Post

  def Posts(request):
    model = Post
    user = User.objects.get(id=request.user.id)
    return render(request, "api/signup.html", {"posts": model, "user": user})

class PostCreateView(CreateView):
  model = Post
  fields = ["title"]
  success_url = reverse_lazy("posts")

  def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class PostUpdateView(UpdateView):
  model = Post
  fields = ["title"]
  success_url = reverse_lazy("posts")

class PostDeleteView(DeleteView):
  model = Post
  success_url = reverse_lazy("posts")

def signUp(request):
    if request.method == "POST": 
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            first_name = form.cleaned_data["name"].lower()
            last_name = form.cleaned_data["surname"].lower()
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            usernameExists = User.objects.filter(username=username).first()
            if usernameExists:
                return HttpResponse("The username already exists.")
            else:
                user = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password,
                )
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect("posts")
        else:
            return HttpResponse("Something went wrong. Try again later.")
    else:
        form = SignUpForm()
        return render(request, "api/signup.html", {"form": form})

def signIn(request):
    form = SignInForm()
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("posts")
        return HttpResponse("Invalid fields!")
    return render(request, "api/signin.html", {"form": form})

def like_post(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=pk)
        if post.likes.filter(id=request.user.id):
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return redirect(request.META.get("HTTP_REFERER"))
    return redirect("")