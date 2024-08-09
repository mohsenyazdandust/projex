from django.db import models


class Student(models.Model):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    telegram_id = models.CharField(max_length=255)
    is_accepted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username