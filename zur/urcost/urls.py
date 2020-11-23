from django.urls import path
from django.conf.urls import url, include
from .views import TagPayCreateView
urlpatterns = [
    path('', TagPayCreateView.as_view(template_name="tag_costs.html")),
]
