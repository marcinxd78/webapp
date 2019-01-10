from django.urls import path
from .views import tag_response
from .views import tag_add
from .views import tag_edit
from .views import tag_delete
from django.conf.urls import url, include
from rest_framework import routers
from .views import TagViewSet

router = routers.DefaultRouter()
router.register(r'tags', TagViewSet, base_name='tags')

urlpatterns = [
    path('tag/', tag_response, name='tag_all'),
    path('new/', tag_add, name='tag_add'),
    path('edit/<int:id>/', tag_edit, name='tag_edit'),
    path('delete/<int:id>/', tag_delete, name='tag_delete'),
    url(r'^', include(router.urls)),

]
