from hero.models import Hero
from django.views.generic import DetailView, ListView


class HeroListView(ListView):
    model = Hero
    template_name = 'hero_list.html'


class HeroDetailView(DetailView):
    model = Hero
    template_name = 'hero_detail.html'
