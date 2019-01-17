from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from account.models import MyUser
from .models import Tag, Department
from .forms import TagForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import TagSerializer, DepartmentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer







@login_required
def tag_response(request):
    tag_views = Tag.objects.all()
    return render(request, 'tag_list.html', {'tag' : tag_views})

@login_required
def tag_add(request):
    form = TagForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(tag_response)

    return render(request, 'tag_form.html', {'new_tag': form})

@login_required
def tag_edit(request, id):
    tag = get_object_or_404(Tag, pk=id)
    form = TagForm(request.POST or None, instance=tag,)

    if form.is_valid():
        form.save()
        return redirect(tag_response)

    return render(request, 'tag_form.html', {'new_tag': form})

@login_required
def tag_delete(request, id):
    form = get_object_or_404(Tag, pk=id)

    if request.method == 'POST':
         form.delete()
         return redirect(tag_response)

    return render(request, 'delete_apply.html', {'tag': form})

@login_required
def tag_index(request):
    return render(request, 'index.html')

