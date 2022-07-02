from django.contrib import admin
from . import models

# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title',) # used for showing the notes ofject as the title of the object, instead of 'Notes object X'
    #pass - enables the standart functionality - basic

#register that the model is attached to the admin model
admin.site.register(models.Notes, NotesAdmin)