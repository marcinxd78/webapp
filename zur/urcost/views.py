from django.shortcuts import render
from .forms import TagToPayForm, PayForTagFormset
from .models import PayForTag, TagToPay
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
# def cost_response(request):
#
#     return render(request, 'tag_list.html', {'tag' : tag_views})

# def create_book_with_authors(request):
#     template_name = 'tag_costs.html'
#     if request.method == 'GET':
#         infopayform = TagToPayForm(request.GET or None)
#         payform = PayForTagFormset(queryset=TagToPay.objects.none())
#     elif request.method == 'POST':
#         infopayform = TagToPayForm(request.POST)
#         payform = PayForTagFormset(request.POST)
#         if infopayform.is_valid() and payform.is_valid():
#             # first save this book, as its reference will be used in `Author`
#             info = infopayform.save()
#             for form in payform:
#                 # so that `book` instance can be attached.
#                 author = form.save(commit=False)
#                 author.info = info
#                 author.save()
#             return redirect('tag_costs.html')
#     return render(request, template_name, {
#         ' infopayform':  infopayform,
#         'payform': payform,
#     })

# def cost_add(request):
#     form = TagToPayForm(request.POST or None, request.FILES or None)
#     form2 = PayForTagFormset(request.POST or None, request.FILES or None)
#     if form.is_valid() & form2.is_valid():
#         form.save()
#         form2.save()
#         return redirect(cost_response)
#
#     return render(request, 'tag_costs.html', {'form': form, 'form2': form2})

class TagPayCreateView(CreateView):
    template_name = 'tag_cost.html'
    model = TagToPay
    form_class = TagToPayForm
    success_url = 'success/'

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