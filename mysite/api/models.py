from django.db import models

# Create your models here.

class Task(models.Model):
    content = models.CharField( max_length=50)
    isComplete = models.BooleanField(default=False, blank=True, null = True)
    
    def __str__(self):
        return self.title
    
