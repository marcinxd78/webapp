from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied

from account.models import MyUser
from .models import Tag, Department
from .forms import TagForm
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import TagSerializer, DepartmentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class TagViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    serializer_class = TagSerializer
    queryset = Tag.objects.all()

    def get_queryset(self):
        if self.request.user.has_perm('ur.view_alltags'):
            return Tag.objects.all()
        elif self.request.user.has_perm('ur.view_mechanic'):
            return Tag.objects.filter(fix_dep__name_fix_cat="Mechaniczny")
        elif self.request.user.has_perm('ur.view_electric'):
            return Tag.objects.filter(fix_dep__name_fix_cat="Elektryczny")
        elif self.request.user.has_perm('ur.view_automatic'):
            return Tag.objects.filter(fix_dep__name_fix_cat="Automatyczny")
        else:
            return None


@login_required
@permission_required('ur.view_tag', raise_exception=True)
def tag_response(request):
    tag_views = Tag.objects.filter(fix_dep__name_fix_cat="Mechaniczny")
    # tag_views = Tag.objects.all()
    return render(request, 'tag_list.html', {'tag': tag_views})


@login_required
@permission_required('ur.add_tag', 'ur.change_tag', raise_exception=True)
def tag_add(request):
    form = TagForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(tag_response)

    return render(request, 'tag_form.html', {'new_tag': form})


@login_required
@permission_required('ur.change_tag', raise_exception=True)
def tag_edit(request, id):
    tag = get_object_or_404(Tag, pk=id)
    form = TagForm(request.POST or None, request.FILES or None, instance=tag, )

    if form.is_valid():
        form.save()
        return redirect(tag_response)

    return render(request, 'tag_form.html', {'new_tag': form})


@login_required
@permission_required('ur.delete_tag', raise_exception=True)
def tag_delete(request, id):
    form = get_object_or_404(Tag, pk=id)

    if request.method == 'POST':
        form.delete()
        return redirect(tag_response)
    raise PermissionDenied()
    return render(request, 'delete_apply.html', {'tag': form})


@login_required
def tag_index(request):
    tag_view = Tag.objects.order_by('-add_date')[:8]
    return render(request, 'index.html', {'card_tag': tag_view})
