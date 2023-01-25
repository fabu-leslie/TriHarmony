from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from .forms import ChildForm
from .models import Child


def home(request):
    return render(request, 'home.html')


def client_list(request):
    clients = Child.objects.all()
    return render(request, 'client_list.html', {'clients': clients})


def add_client(request):
    if request.method == 'POST':
        new_client_form = ChildForm(request.POST)
        if new_client_form.is_valid():
            new_client_form.save()
            return HttpResponseRedirect(reverse('specialist:client_list'))
    else:
        new_client_form = ChildForm()
    return render(request, 'add_client.html', {'new_client_form': new_client_form})
