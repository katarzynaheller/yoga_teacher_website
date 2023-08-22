from django.db import models


class Yoga_Retreat(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField()
