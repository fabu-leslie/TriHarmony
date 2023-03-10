from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from .forms import ChildForm, BehaviorForm, SpecialistBehaviorForm
from .models import Child, Behavior


def add_behavior(request, client_id):
    client = get_object_or_404(Child, pk=client_id)
    if request.method == 'POST':
        form = BehaviorForm(request.POST)
        if form.is_valid():
            new_behavior = form.save(commit=False)
            new_behavior.child = client
            new_behavior.save()
            return HttpResponseRedirect(reverse('specialist:client_detail', args=(client_id,)))
    else:
        form = BehaviorForm()
    return render(request, 'add_behavior.html', {'form': form, 'client': client})


def add_client(request):
    if request.method == 'POST':
        new_client_form = ChildForm(request.POST)
        if new_client_form.is_valid():
            new_client_form.save()
            return HttpResponseRedirect(reverse('specialist:client_list'))
    else:
        new_client_form = ChildForm()
    return render(request, 'add_client.html', {'new_client_form': new_client_form})


def client_behavior(request, client_id):
    client = Child.objects.get(id=client_id)
    behaviors = Behavior.objects.filter(child=client)
    context = {'client': client, 'behaviors': behaviors}
    return render(request, 'client_detail.html', context)


def client_detail(request, client_id):
    behavior_form = SpecialistBehaviorForm()
    client = get_object_or_404(Child, pk=client_id)
    if request.user.is_authenticated and request.user.has_perm('parent_data_form'):
        behaviors = Behavior.objects.filter(child=client)
        return render(request, 'client_detail.html', {'client': client, 'behaviors': behaviors})
    return render(request, 'client_detail.html', {'client': client, 'behavior_form': behavior_form})


def client_list(request):
    clients = Child.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

def edit_target_behaviors(request, client_id):
    client = get_object_or_404(Child, id=client_id)
    if request.method == "POST":
        form = SpecialistBehaviorForm(request.POST, instance=client.behavior)
        if form.is_valid():
            form.save()
            return redirect('client_detail', client_id)
    else:
        form = SpecialistBehaviorForm(instance=client.behavior)
    return render(request, 'edit_target_behaviors.html', {'form': form, 'client': client})


def home(request):
    return render(request, 'home.html')


def parent_detail(request, client_id):
    client = get_object_or_404(Child, pk=client_id)
    if request.user.is_authenticated:
        behavior_form = BehaviorForm()
        return render(request, 'parent_detail.html', {'client': client, 'behavior_form': behavior_form})
    else:
        return render(request, 'parent_detail.html', {'client': client})


def parent_data_form(request, client_id):
    # retrieves behavior with given id from db, uses it to pre-populate a behavior form.
    behavior = get_object_or_404(Behavior, pk=client_id)
    if request.method == 'POST':
        form = BehaviorForm(request.POST, instance=behavior)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('specialist:client_detail', args=(client_id,)))
    else:
        form = BehaviorForm(instance=behavior)
    return render(request, 'parent_data_form.html', {'form': form, 'behavior': behavior})



