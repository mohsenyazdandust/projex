from django.db import models

import datetime

class Student(models.Model):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    telegram_id = models.CharField(max_length=255)
    is_accepted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    

class Exercise(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title


class Session(models.Model):
    date = models.DateField(default=datetime.date.today)
    exercises = models.ManyToManyField(Exercise, blank=True)
    presents = models.ManyToManyField(Student, blank=True)
    
    def __str__(self):
        return str(self.date)
    

class Submitted(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    answer = models.TextField()
    feedback = models.TextField()
    
    def __str__(self):
        return str(self.exercise)