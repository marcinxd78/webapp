from django.urls import path
from django.conf.urls import url, include
from .views import TagPayCreateView, RecipeUpdateView, TagToPayListView
urlpatterns = [
    path('', TagPayCreateView.as_view(template_name="tag_costs.html")),
    path('update/<pk>/', RecipeUpdateView.as_view(template_name="tag_costs.html")),
    path('list/', TagToPayListView.as_view(template_name="cost_list_view.html")),
]
