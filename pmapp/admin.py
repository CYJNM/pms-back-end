from django.contrib import admin
from .models import Server, Project, QualityRecord, CollectionRecord
# Register your models here.


@admin.register(Server, Project, QualityRecord, CollectionRecord)
class PersonAdmin(admin.ModelAdmin):
    pass

