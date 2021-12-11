"""vaibhav URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from os import name

from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("form/", views.form, name="form"),
    path("add_deatil/", views.add_deatil, name="add_deatil"),
    path("all_deatil/", views.all_deatil, name="all_deatil"),
    path("edit_deatil/<int:id>", views.edit_deatil, name="edit_deatil"),
    path("update_deatil/<int:id>", views.update_deatil, name="update_deatil"),
    path("delete_deatil/<int:id>", views.delete_deatil, name="delete_deatil"),
]
