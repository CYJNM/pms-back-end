from django.contrib import admin
from .models import Server, Project, QualityRecord, CollectionRecord, User
# Register your models here.


@admin.register(User, Server, Project, QualityRecord, CollectionRecord)
class PersonAdmin(admin.ModelAdmin):
    pass

