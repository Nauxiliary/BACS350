from django.views.generic import TemplateView

class SuperManView(TemplateView):
    template_name = 'super_man.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'About this Class', 
            'body': 'Once upon a time ...',
        }

class HawkGirlView(TemplateView):
    template_name = 'hawk_girl.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'My Home Page', 
            'body': 'This page is boring ...',
        }

class FlashView(TemplateView):
    template_name = 'flash.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Index Page', 
            'body': 'Begin here',
        }