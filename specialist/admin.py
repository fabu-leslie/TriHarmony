from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Behavior, Child, Parent, Specialist, BehaviorCheckIn





admin.site.register(Specialist)
admin.site.register(Child)
admin.site.register(Parent)
admin.site.register(Behavior)
admin.site.register(BehaviorCheckIn)
