from django.db import models
from django.contrib.auth.models import User

class Journal(models.Model):
    title = models.CharField(max_length=100) # a field for the journal title
    body = models.TextField() # a field for the journal body
    user = models.ForeignKey(User, on_delete=models.CASCADE) # a field for the user who created the journal
    password = models.CharField(max_length=20) # a field for the journal password

    def __str__(self):
        return self.title # a method to return the journal title as the string representation
