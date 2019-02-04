from django.contrib import admin

from django.contrib import admin
from . models import Snippet
# register model here

class SnippetAdmin(admin.ModelAdmin):
    readonly_fields = ('highlighted',)


admin.site.register(Snippet, SnippetAdmin)