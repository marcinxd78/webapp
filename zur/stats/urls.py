from django.urls import path
from django.conf.urls import url, include
from .views import graph
from . import views
from django.utils.translation import gettext_lazy as _
urlpatterns = [
    path('stats/', graph, name='graph.html'),
]