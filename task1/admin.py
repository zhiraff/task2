from django.contrib import admin

from .models import MyFiles

#class MyFilesAdmin(admin.ModelAdmin):
#    list_display = ['id', 'file_name', 'file_data']
#
#admin.site.register(MyFiles, MyFilesAdmin)

admin.site.register(MyFiles)