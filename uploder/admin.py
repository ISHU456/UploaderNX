from django.contrib import admin
from .models import Document
# Register your models here.


class DocumentAdmin(admin.ModelAdmin):
    list_display =['name','files','addDate']

admin.site.register(Document,DocumentAdmin)