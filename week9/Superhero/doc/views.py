from django.views.generic import RedirectView, TemplateView


class DocumentView(TemplateView):
    template_name = 'document.html'
