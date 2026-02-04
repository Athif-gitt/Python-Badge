from django.db import models

class Person(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Doctor(Person):
    specialization = models.CharField(max_length=100)

    # class Meta:
    #     proxy = True
    #     ordering = ['-age']

class Patient(Person):
    disease = models.CharField(max_length=200)


