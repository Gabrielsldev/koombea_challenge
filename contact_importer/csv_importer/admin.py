from django.contrib import admin
from csv_importer.models import csvFile, Contact

# Register your models here.



class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ('user', 'created_at',)
    list_filter = ('user', 'created_at',)

admin.site.register(Contact, ContactAdmin)


class csvFileAdmin(admin.ModelAdmin):
    model = csvFile
    list_display = ('name', 'user', 'uploaded_at',)
    list_filter = ('user', 'uploaded_at',)

admin.site.register(csvFile, csvFileAdmin)