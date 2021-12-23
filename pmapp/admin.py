from django.contrib import admin
from .models import Server, Project, QualityRecord, CollectionRecord, User, Menu
# Register your models here.


@admin.register(User, Server, Project, QualityRecord, CollectionRecord, Menu)
class PersonAdmin(admin.ModelAdmin):
    pass

