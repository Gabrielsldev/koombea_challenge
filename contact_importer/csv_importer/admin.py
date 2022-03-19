from django.contrib import admin
from csv_importer.models import csvFile, Contact

# Register your models here.

admin.site.register(csvFile)
admin.site.register(Contact)