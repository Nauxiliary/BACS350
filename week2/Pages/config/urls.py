from django.urls import path
from django.views.generic import AboutView, HomeView, IndexView

urlpatterns = [
    path('about', AboutView.as_view()),
    path('home', HomeView.as_view()),
    path('', IndexView.as_view()),
]
