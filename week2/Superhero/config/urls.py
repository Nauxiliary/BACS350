from django.urls import path
from hero.views import SuperManView, HawkGirlView, FlashView

urlpatterns = [
    path('', SuperManView.as_view()),
    path('superman', SuperManView.as_view()),
    path('hawkgirl', HawkGirlView.as_view()),
    path('flash', FlashView.as_view()),
]