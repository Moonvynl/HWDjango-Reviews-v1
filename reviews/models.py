from django.db import models

class Review(models.Model):
    username = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)