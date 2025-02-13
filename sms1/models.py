from django.db import models

# Create your models here.
class Destination(models.Model):
    SCHOOL_LEVEL_CHOICES = [
        ('Pre-Primary', 'Pre-Primary'),
        ('Primary', 'Primary'),
        ('Secondary', 'Secondary'),
        ('Tertiary', 'Tertiary'),
    ]

    name = models.CharField(max_length=255)
    level = models.CharField(max_length=20, choices=SCHOOL_LEVEL_CHOICES)
    location = models.CharField(max_length=255)
    num_students = models.IntegerField()

    def _str_(self):
        return self.name