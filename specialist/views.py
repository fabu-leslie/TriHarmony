from django.shortcuts import redirect, render
from .models import Behavior, BehaviorCheckIn, Child, Parent
from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .forms import BehaviorForm, ChildForm, FeelingForm, SpecialistBehaviorForm
from .models import Behavior, BehaviorCheckIn, Child, Feeling, Parent


# @login_required
@permission_required('specialist.view_specialist')
def add_behavior(request, client_id):
    client = get_object_or_404(Child, pk=client_id)
    if request.method == 'POST':
        form = SpecialistBehaviorForm(request.POST)
        if form.is_valid():
            new_behavior = form.save(commit=False)
            new_behavior.child = client
            new_behavior.save()
            return HttpResponseRedirect(reverse('specialist:client_detail', args=(client_id,)))
    else:
        form = SpecialistBehaviorForm()
    return render(request, 'add_behavior.html', {'form': form, 'client': client})


# @login_required
@permission_required('specialist.view_specialist')
def add_client(request):
    if request.method == 'POST':
        new_client_form = ChildForm(request.POST)
        if new_client_form.is_valid():
            new_client_form.save()
            return HttpResponseRedirect(reverse('specialist:client_list'))
    else:
        new_client_form = ChildForm()
    return render(request, 'add_client.html', {'new_client_form': new_client_form})


# @login_required
def client_behavior(request, client_id):
    client = Child.objects.get(id=client_id)
    behaviors = Behavior.objects.filter(child=client)
    context = {'client': client, 'behaviors': behaviors}
    return render(request, 'client_detail.html', context)


# @login_required
@permission_required('specialist.view_specialist')
def client_detail(request, client_id):
    client = get_object_or_404(Child, id=client_id)
    behaviors = client.behavior_set.all()
    parent = client.parent_set.all()
    notes = client.behavior_set.all()
    context = {
        'client': client,
        'behaviors': behaviors,
        'parent': parent,
        'notes': notes,
    }
    return render(request, 'client_detail.html', context)


# @login_required
@permission_required('specialist.view_specialist')
def client_list(request):
    clients = Child.objects.all().order_by('name')
    return render(request, 'client_list.html', {'clients': clients})

# @permission_required('specialist.view_specialist')
# def client_list(request):
#     specialist = request.user.specialist
#     clients = Child.objects.filter(specialist=specialist)
#     return render(request, 'client_list.html', {'clients': clients})

# @permission_required('specialist.view_specialist')
# def client_list(request):
#     show_all = request.GET.get('show_all')
#     if show_all:
#         clients = Child.objects.all()
#     else:
#         specialist = request.user.specialist
#         clients = Child.objects.filter(specialist=specialist)
#     return render(request, 'client_list.html', {'clients': clients})

# @login_required


@permission_required('specialist.view_specialist')
def edit_target_behaviors(request, behavior_id):
    behavior = get_object_or_404(Behavior, id=behavior_id)
    child = behavior.child
    if request.method == 'POST':
        form = SpecialistBehaviorForm(request.POST, instance=behavior)
        if form.is_valid():
            form.save()
            messages.success(request, 'Target behavior updated')
            return HttpResponseRedirect(reverse('specialist:client_detail', args=[behavior.child.id]))
    else:
        form = SpecialistBehaviorForm(instance=behavior)
    return render(request, 'edit_target_behaviors.html', {'form': form, 'child': child})


def home(request):
    return render(request, 'home.html')


@login_required
@permission_required('specialist.view_parent')
def parent_detail(request, parent_id):
    parent = get_object_or_404(Parent, id=parent_id)
    child = parent.child
    behaviors = Behavior.objects.filter(child=child)
    checkins = BehaviorCheckIn.objects.filter(behavior__child=child)
    specialist = child.specialist

    if request.method == 'POST':
        form = BehaviorForm(request.POST)
        if form.is_valid():
            behavior = form.cleaned_data['behavior']
            behavior_intensity = form.cleaned_data['behavior_intensity']
            behavior_frequency = form.cleaned_data['behavior_frequency']
            note = form.cleaned_data['note']
            new_checkin = BehaviorCheckIn.objects.create(
                behavior=behavior,
                behavior_intensity=behavior_intensity,
                behavior_frequency=behavior_frequency,
                note=note
            )
            messages.success(request, 'Your form was submitted successfully!')
            return redirect('specialist:parent_detail', parent_id=parent_id)
    else:
        form = BehaviorForm()

    context = {
        'parent': parent,
        'child': child,
        'behaviors': behaviors,
        'checkins': checkins,
        'form': form,
        'specialist': specialist,
    }
    return render(request, 'parent_detail.html', context)

# @login_required


@permission_required('specialist.view_child')
def record_feeling(request, client_id):
    child = get_object_or_404(Child, id=client_id)
    parent = child.parent_set.all()
    if request.method == 'POST':
        form = FeelingForm(request.POST)
        if form.is_valid():
            feeling = form.save(commit=False)
            feeling.child = child
            feeling.feeling = form.cleaned_data['feeling']
            feeling.note = form.cleaned_data['note']
            feeling.save()
            messages.success(
                request, 'Great job! Thank you for sharing your feelings!')
            return HttpResponseRedirect(reverse('specialist:record_feeling', args=(client_id,)))
        else:
            messages.error(request, 'Oops! You forgot to select a feeling!')
    else:
        form = FeelingForm()
    context = {
        'form': form,
        'child': child,
        'parent': parent, }
    return render(request, 'record_feeling.html', context)

# @login_required


@permission_required('specialist.view_specialist')
def view_feelings(request, client_id):
    child = get_object_or_404(Child, id=client_id)
    feelings = Feeling.objects.filter(child=child)
    behaviors = BehaviorCheckIn.objects.filter(behavior__child=child)
    context = {
        'feelings': feelings,
        'child': child,
        'behaviors': behaviors,
    }

    return render(request, 'view_feelings.html', context)


# @login_required
@permission_required('specialist.view_specialist')
def search_results(request):
    query = request.GET.get('q')
    if query:
        clients = Child.objects.filter(name=query).values()
    else:
        clients = Child.objects.all()
    print(clients)
    return render(request, 'search_results.html', {'clients': clients})

@permission_required('specialist.view_parent')
def parent_list(request):
    if request.user.is_authenticated:
        current_user = request.user
        try:
            parent = Parent.objects.get(user=current_user)
            children = Child.objects.filter(parent=parent)
            return render(request, 'parent_list.html', {'children': children})
        except Parent.DoesNotExist:
            return render(request, 'no_children.html')
    else:
        return redirect('login')
