from django.db import models
from django.contrib.auth.models import User
from tinymce.widgets import TinyMCE

# Create your models here.

class Lab(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    start_date = models.DateField()
    due_date = models.DateField()
    users = models.ManyToManyField(User)
    completed = models.BooleanField(default=False)

    class Meta: 
        verbose_name_plural = 'Labs'

    def __str__(self):
        return self.title

class Todo(models.Model):
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)
    lab = models.ForeignKey(Lab, default=1, verbose_name=("Lab"), on_delete=models.SET_DEFAULT)
    
    class Meta: 
        verbose_name_plural = 'Todos'

    def __str__(self):
        return self.title