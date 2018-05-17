from django.contrib import admin
from .models import Project, Advert


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'username']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Advert)
