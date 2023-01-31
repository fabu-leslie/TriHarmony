from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from .forms import ChildForm, BehaviorForm, SpecialistBehaviorForm
from .models import Child, Behavior, BehaviorCheckIn, Parent


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
    client = get_object_or_404(Child, id=client_id)
    behaviors = client.behavior_set.all()
    context = {
        'client': client,
        'behaviors': behaviors,
    }
    return render(request, 'client_detail.html', context)

# def client_detail(request, pk):
#     child = Child.objects.get(pk=pk)
#     behaviors = Behavior.objects.filter(child_behaviors = child)
#     context = {'child': child, 'behaviors': behaviors}
#     return render(request, 'client_detail.html', context)


def client_list(request):
    clients = Child.objects.all()
    return render(request, 'client_list.html', {'clients': clients})


def edit_target_behaviors(request, client_id):
    child = get_object_or_404(Child, id=client_id)
    if request.method == 'POST':
        form = SpecialistBehaviorForm(request.POST)
        if form.is_valid():
            form.save(child)
            return redirect('specialist:client_detail', client_id=client_id)
    else:
        behaviors = child.behaviors.all()
        form = SpecialistBehaviorForm(initial={
            'behavior1': behaviors[0].behavior if behaviors else '',
            'behavior2': behaviors[1].behavior if len(behaviors) > 1 else '',
            'behavior3': behaviors[2].behavior if len(behaviors) > 2 else '',
        })
    return render(request, 'edit_target_behaviors.html', {'form': form})


def home(request):
    return render(request, 'home.html')


def parent_detail(request, parent_id):
    parent = get_object_or_404(Parent, id=parent_id)
    child = parent.child
    behaviors = Behavior.objects.filter(child=child)[0]
    behaviors_filter = Behavior.objects.filter(child=child)[:1] #filtering behaviorcheckin objects
    new_parent_data = BehaviorCheckIn.objects.filter(behavior=behaviors_filter)
    print(new_parent_data)
    if request.method == 'POST':
        form = BehaviorForm(request.POST)
        if form.is_valid():
            new_checkin = form.save(commit=False)
            new_checkin.behavior = behaviors
            new_checkin.save()
            form.save_m2m()
            return redirect('specialist:parent_detail', parent_id=parent_id)
    else:
        form = BehaviorForm()
    context = {
        'parent': parent,
        'child': child,
        'behaviors': behaviors,
        'checkins': new_parent_data.last(),
        'form': form,
    }
    # print(behaviors.behaviorcheckin_set.all())
    return render(request, 'parent_detail.html', context)

