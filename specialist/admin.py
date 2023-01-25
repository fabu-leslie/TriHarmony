from django.contrib import admin
from .models import Behavior, Child, Parent, Specialist

admin.site.register(Specialist)
admin.site.register(Child)
admin.site.register(Parent)
admin.site.register(Behavior)
