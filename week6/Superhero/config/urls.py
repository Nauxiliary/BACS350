"""config URL Configuration

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
from django.contrib import admin
from django.urls import path
from hero.views import HeroView, HeroDetailView, HeroListView, HeroCreateView, HeroUpdateView, HeroDeleteView

urlpatterns = [
    path('admin/',                  admin.site.urls),
    path('',                        HeroView.as_view()),
    path('<int:pk>/',               HeroDetailView.as_view()),
    path('hero/',                   HeroListView.as_view(),    name='hero_list'),
    path('hero/<int:pk>/',          HeroDetailView.as_view(),  name='hero_detail'),
    path('hero/add',                HeroCreateView.as_view(),  name='hero_add'),
    path('hero/<int:pk>/edit',      HeroUpdateView.as_view(),  name='hero_edit'),
    path('hero/<int:pk>/delete',    HeroDeleteView.as_view(),  name='hero_delete'),
]
