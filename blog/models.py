from django.db import models
from django.utils import timezone
# Create your models here.

class blog(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=400)
    desc = models.TextField(null=True, blank=True)
    published_date = models.DateTimeField(default=timezone.now)  # Fixed the default value for DateTimeField
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=196)
    message = models.TextField()

    def __str__(self):
        return self.email