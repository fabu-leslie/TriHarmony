from django.contrib import admin
from .models import Child, Parent, Specialist

admin.site.register(Specialist)
admin.site.register(Child)
admin.site.register(Parent)
