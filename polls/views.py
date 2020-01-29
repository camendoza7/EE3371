from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Description, Category


def index(request, ec = ''):
    categories = Category.objects.all()
    context = {'categories' : categories, 'ec' : ec}
    return render(request, 'polls/index.html', context)

def record(request):
    context = {}
    text = request.POST['Description']
    try:
        pk = request.POST['choice']
    except KeyError:
        return redirect('polls:index', ec = 'caterr')
    c = Category.objects.get(pk = pk)
    c.votes += 1
    c.save()
    d = Description(text = text, category = c)
    d.save()


    context['categories'] = Category.objects.all()

    return render(request, 'polls/submitted.html', context)