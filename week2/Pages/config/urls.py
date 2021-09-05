from django.urls import path
from pages.views import AboutView, HomeView, IndexView

urlpatterns = [
    path('about', AboutView.as_view()),
    path('home', HomeView.as_view()),
    path('', IndexView.as_view()),
]
