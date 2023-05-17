from django.shortcuts import render
from app.forms import *
from django.views.generic import FormView
from django.http import HttpResponse
# Create your views here.
class cbv_form(FormView):
    form_class=Schoolform
    template_name='cbv_form.html'

    def form_valid(self, form):
        form.save()
        return HttpResponse('data is saved')