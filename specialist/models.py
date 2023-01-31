from django.db import models


class Specialist(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    is_specialist = True

    def __str__(self):
        return self.name


class Child(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=255)
    specialist = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Behavior(models.Model):
    behavior1 = models.CharField(max_length=255)
    behavior1_details = models.CharField(max_length=1000, default='')
    behavior2 = models.CharField(max_length=255)
    behavior2_details = models.CharField(max_length=1000, default='')
    behavior3 = models.CharField(max_length=255)
    behavior3_details = models.CharField(max_length=1000, default='')
    notes = models.CharField(max_length=255)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)

    def __str__(self):
        return self.behavior1


class BehaviorCheckIn(models.Model):
    behavior1_intensity = models.IntegerField()
    behavior1_frequency = models.IntegerField()
    behavior2_intensity = models.IntegerField()
    behavior2_frequency = models.IntegerField()
    behavior3_intensity = models.IntegerField()
    behavior3_frequency = models.IntegerField()
    behavior = models.ForeignKey(Behavior, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return str(self.behavior1_intensity)


class Parent(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    child = models.ForeignKey(Child, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
