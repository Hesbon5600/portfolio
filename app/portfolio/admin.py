from django.contrib import admin
from .models import Project, Category, Client
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from django_better_admin_arrayfield.forms.widgets import DynamicArrayTextareaWidget
from django_better_admin_arrayfield.forms.fields import DynamicArrayField


# Register your models here.
admin.site.register(Category)
admin.site.register(Client)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin, DynamicArrayMixin):
    formfield_overrides = {
        DynamicArrayField: {'widget': DynamicArrayTextareaWidget},
    }
