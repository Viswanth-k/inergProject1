
from django.contrib import admin
from .models import Xlss, Sum
from import_export.admin import ImportExportModelAdmin

@admin.register(Xlss)
class userdat(ImportExportModelAdmin):
    pass

admin.site.register(Sum)