from hero.models import Hero
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, RedirectView


class HeroView(RedirectView):
    url = '/hero/'


class HeroListView(ListView):
    model = Hero
    template_name = 'hero_list.html'


class HeroDetailView(DetailView):
    model = Hero
    template_name = 'hero_detail.html'


class HeroCreateView(CreateView):
    template_name = "hero_add.html"
    model = Hero
    fields = ['name', 'identity', 'description',
              'strength', 'weakness', 'image']


class HeroUpdateView(UpdateView):
    template_name = "hero_edit.html"
    model = Hero
    fields = ['name', 'identity', 'description',
              'strength', 'weakness', 'image']


class HeroDeleteView(DeleteView):
    model = Hero
    template_name = 'hero_delete.html'
    success_url = reverse_lazy('hero_list')
