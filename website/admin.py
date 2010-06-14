from django.contrib import admin
from website.models import Entry
from tinymce.widgets import AdminTinyMCE
from django.db import models

class EntryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminTinyMCE},
    }


admin.site.register(Entry, EntryAdmin)
