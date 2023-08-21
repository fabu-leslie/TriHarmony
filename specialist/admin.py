from django.contrib import admin
from .forms import CustomParentForm
# from django.contrib.auth.admin import UserAdmin
from .models import Behavior, Child, Parent, Specialist, BehaviorCheckIn, Feeling


class ParentAdmin(admin.ModelAdmin):
    form = CustomParentForm
    list_display = ('name', 'email', 'display_children')

    def display_children(self, obj):
        return ", ".join([child.name for child in obj.child.all()])

    display_children.short_description = 'Children'


admin.site.register(Specialist)
admin.site.register(Child)
admin.site.register(Parent, ParentAdmin)
admin.site.register(Behavior)
admin.site.register(BehaviorCheckIn)
admin.site.register(Feeling)
# admin.site.register(UserAdmin)
