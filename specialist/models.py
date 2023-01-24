from django.db import models

class Specialist(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
