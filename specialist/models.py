from django.db import models


class Specialist(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Child(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=255)
    specialist = models.CharField(max_length=255)  # ?

    def __str__(self):
        return self.name


class Parent(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    child = models.ForeignKey(Child, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
