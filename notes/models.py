#own imports
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    #add foreign key to the user
    user =  models.ForeignKey(User, on_delete=models.CASCADE,related_name="notes") #connects it to the user model, delete all notes on user deletion,