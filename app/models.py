from django.db import models


# Create your models here.
class Patient(models.Model):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField(default=18)
    gender = models.CharField(
        max_length=1, choices=GENDERS, default='M')
    note = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Patient ID: {self.pk} - {self.name}"
