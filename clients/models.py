from __future__ import unicode_literals

from django.db import models


class Pet(models.Model):

    animal_choices = (
        ('CA', 'cat'),
        ('DO', 'dog'),
        ('RA', 'rabbit'),
    )
    name = models.CharField(max_length=25)
    animal = models.CharField(max_length=2, choices=animal_choices)
    breed = models.CharField(max_length=20)  # arbitrary length..
