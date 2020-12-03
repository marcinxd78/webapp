from django.shortcuts import render
from django.http import HttpResponse
from .forms import TagToPayForm, PayForTagFormset
from .models import PayForTag, TagToPay
from django.views.generic import CreateView, UpdateView, ListView
from django.http import HttpResponseRedirect
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.db.models import  Sum
from django.db.models import F, FloatField
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
import weasyprint
from django.conf import settings
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

@staff_member_required
def admin_payment_detail(request, payment_id):
    payview = get_object_or_404(PayForTag , id=payment_id)
    return render(request,'pay_detail.html', {'payview': payview})

@login_required
@staff_member_required
def admin_order_detail(request, order_id):
    order1 = TagToPay.objects.get(pk=order_id)
   # order = get_object_or_404(TagToPay, pk=order_id)
    #print(order)
    #order = PayForTag.objects.get(id=order_id)
    order = PayForTag.objects.filter(tag_order_id=order_id)
    total = order.aggregate(total_price=Sum( F('cost_material') * F('amount_material'),output_field=FloatField()))
    total_conv = total['total_price']
    print(total_conv)
    #order = Pay.objects.get(pk=order_id)
    #order = get_object_or_404(PayForTag, tag_order_id=order_id)
    print(order)
    #order = get_object_or_404(TagToPay , id=order_id)
    return render(request,'pay_detail.html', {'order': order,
                                              'order1': order1,
                                              'total_conv': total_conv})
def admin_order_pdf(request, order_id):
     order1 = TagToPay.objects.get(pk=order_id)
     order = PayForTag.objects.filter(tag_order_id=order_id)
     total = order.aggregate(total_price=Sum(F('cost_material') * F('amount_material'), output_field=FloatField()))
     total_conv = total['total_price']
     html = render_to_string('pdf.html',
     {'order': order, 'order1': order1, 'total_conv': total_conv})
     response = HttpResponse(content_type='application/pdf')
     response['Content-Disposition'] = 'filename=\
     "order1_{}.pdf"'.format(order1.id)
     weasyprint.HTML(string=html).write_pdf(response,)
     return response