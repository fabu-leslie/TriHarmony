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


class Behavior(models.Model):
    behavior1 = models.CharField(max_length=255)
    behavior1_intensity = models.IntegerField()
    behavior1_frequency = models.IntegerField()
    behavior2 = models.CharField(max_length=255)
    behavior2_intensity = models.IntegerField()
    behavior2_frequency = models.IntegerField()
    behavior3 = models.CharField(max_length=255)
    behavior3_intensity = models.IntegerField()
    behavior3_frequency = models.IntegerField()
    notes = models.CharField(max_length=255)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)