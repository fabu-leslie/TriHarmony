from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = "registration/signup.html"


class CustomLoginView(LoginView):
    template_name = "registration/login.html"

    def get_success_url(self):
        user = self.request.user
        if user.has_perm('specialist.view_specialist'):
            return reverse_lazy(
                'specialist:home')
        elif user.has_perm('specialist.view_parent'):
            return reverse_lazy(
                'specialist:child_list', kwargs={'parent_id': user.parent.id})
        elif user.has_perm('specialist.view_child'):
            return reverse_lazy(
                'specialist:record_feeling', kwargs={'client_id': user.child.id})
