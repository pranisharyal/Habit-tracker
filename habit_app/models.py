from django.db import models

# Create your models here.

class Habit(models.Model):
    name = models.CharField(max_length=100)
    streak = models.IntegerField(default=0)
    last_marked_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
