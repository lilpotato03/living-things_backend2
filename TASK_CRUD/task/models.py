from django.db import models

# Create your models here.

class Note(models.Model):
    title=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    user=models.CharField(max_length=100)

    def __str__(self):
        return self


class Task(models.Model):
    content=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.CharField(max_length=100)
    checked=models.BooleanField(default=False)
    note=models.ForeignKey(Note,related_name='tasks',on_delete=models.CASCADE)

    def __str__(self):
        return self
