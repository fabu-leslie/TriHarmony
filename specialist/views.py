from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ChildForm

def home(request):
    return render(request, 'home.html')

def add_client(request):
    if request.method == 'POST':
        form = ChildForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ChildForm()
    return render(request, 'add_client.html', {'form': form})
