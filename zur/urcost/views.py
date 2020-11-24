from django.shortcuts import render
from .forms import TagToPayForm, PayForTagFormset
from .models import PayForTag, TagToPay
from django.views.generic import CreateView, UpdateView, ListView
from django.http import HttpResponseRedirect
from django.db import transaction

class TagToPayListView(ListView):
    model = TagToPay
    paginate_by = 100
    context_object_name = ''
    template_name = 'cost_list_view.html'

class TagPayCreateView(CreateView):
    template_name = 'tag_cost.html'
    model = TagToPay
    form_class = TagToPayForm
    success_url = '/costs/list/'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ingredient_form = PayForTagFormset()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  ingredient_form=ingredient_form,))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ingredient_form = PayForTagFormset(self.request.POST)
        if (form.is_valid() and ingredient_form.is_valid() and
            ingredient_form.is_valid()):
            return self.form_valid(form, ingredient_form)
        else:
            return self.form_invalid(form, ingredient_form, )

    def form_valid(self, form, ingredient_form,):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        ingredient_form.instance = self.object
        ingredient_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, ingredient_form,):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  ingredient_form=ingredient_form,
                                  ))


class RecipeUpdateView(UpdateView):

    model = TagToPay
    form_class = TagToPayForm
    success_url = '/costs/list/'

    def get_context_data(self, **kwargs):
        form = super(RecipeUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            form['ingredient_form'] = PayForTagFormset(
                self.request.POST, instance=self.object)

        else:
            form['ingredient_form'] = PayForTagFormset(instance=self.object)

        return form

    def form_valid(self, form):
        print("am I valid tho")
        context = self.get_context_data()
        ingredient_form = context['ingredient_form']

        with transaction.atomic():
            self.object = form.save()

            if ingredient_form.is_valid():
                ingredient_form.instance = self.object
                ingredient_form.save()



        return super(RecipeUpdateView, self).form_valid(form)

    def form_invalid(self, form, ingredient_form, ):

        return self.render_to_response(
            self.get_context_data(form=form,
                                  ingredient_form=ingredient_form,
                                  ))