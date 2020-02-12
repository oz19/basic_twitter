from django.views.generic import TemplateView


class TwitterView(TemplateView):
    template_name = 'tweets/index.html'
