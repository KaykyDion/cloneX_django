"""
URL configuration for cloneX project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from api.views import PostView, PostCreateView, PostUpdateView, PostDeleteView, signUp, signIn, like_post

urlpatterns = [
    path("admin/", admin.site.urls),
    path("feed", PostView.as_view(), name="posts"),
    path("create", PostCreateView.as_view(), name="post_form"),
    path("update/<int:pk>", PostUpdateView.as_view(), name="post_update"),
    path("delete/<int:pk>", PostDeleteView.as_view(), name="post_delete"),
    path("", signUp, name="sign_up"),
    path("signIn", signIn, name="sign_in"),
    path("like/<int:pk>/", like_post, name="like_post"),
]
