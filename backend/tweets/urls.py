from django.urls import path

from .views import TwitterView


urlpatterns = [
    path('', TwitterView.as_view(), name='index'),
]
