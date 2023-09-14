from django.db import models
from django.contrib.auth.models import User


class YogaClass(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    slots = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "yoga class"
        verbose_name_plural = "yoga classes"


class Booking(models.Model):
    STATUS_CHOICES = [
        ("zapisano", "Zapisano"),
        ("odwołano", "Odwołano"),
    ]
    yoga_class = models.ForeignKey(YogaClass, on_delete=models.CASCADE)
    email = models.EmailField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="zapisano")

    def __str__(self):
        return f"{self.yoga_class.name} - {self.email}"
