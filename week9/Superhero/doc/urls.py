from django.views.generic import RedirectView
from django.urls.conf import include, include
from django.contrib import admin
from django.urls import path
from .views import DocumentView

urlpatterns = [
    path('doc', DocumentView.as_view(), name='document'),
]