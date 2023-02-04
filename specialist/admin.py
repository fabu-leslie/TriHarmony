from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import Behavior, Child, Parent, Specialist, BehaviorCheckIn, Feeling


admin.site.register(Specialist)
admin.site.register(Child)
admin.site.register(Parent)
admin.site.register(Behavior)
admin.site.register(BehaviorCheckIn)
admin.site.register(Feeling)
# admin.site.register(UserAdmin)
