from django.urls import path
from django.conf.urls import url, include
from .views import TagPayCreateView, RecipeUpdateView, TagToPayListView, admin_order_detail
from . import views
from django.utils.translation import gettext_lazy as _
urlpatterns = [
    path('add/', TagPayCreateView.as_view(template_name="tag_costs.html")),
    path('update/<pk>/', RecipeUpdateView.as_view(template_name="tag_costs.html")),
    path('list/', TagToPayListView.as_view(template_name="cost_list_view.html")),
    path('admin/order/<int:order_id>/', views.admin_order_detail, name='admin_order_detail'),
    path('admin/order/<int:order_id>/pdf/', views.admin_order_pdf, name='admin_order_pdf'),


]
