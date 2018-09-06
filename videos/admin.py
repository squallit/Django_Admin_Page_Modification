from django.contrib import admin

# Register your models here.
from . import models



class MovieAdmin(admin.ModelAdmin):

    #field that in order displayed
    fields = ["released_year","title","length"]

    #search field in db
    search_fields = ['title',"length"]

    #add a filter as a sidebar
    list_filter = ['released_year','length','title']

    #add headers for data displayed in listview
    list_display = ["released_year","title","length"]

    #allow edit in listview
    list_editable = ["length"]

admin.site.register(models.Customer)
admin.site.register(models.Movie,MovieAdmin)
