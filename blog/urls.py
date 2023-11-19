"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from blog.views import *


urlpatterns = [
    path('',home,name='home'),
    path('blog/<slug:url>/',blog,name='blog'),
    path('category/<slug:url>/',category,name='category'),
    path('add_category/',addCategory),
    path('add_blog/',addBlog),
    path('Login/',Login),
    path('Admin/',Admin),
    path('About/',About)

]

