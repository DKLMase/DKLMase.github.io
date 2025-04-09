from django.db import models
from django.contrib.auth.models import User

class DailyTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    day = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    reminder = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class TutorialSchedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.CharField(max_length=100)
    day = models.CharField(max_length=20)
    time = models.TimeField()
    venue = models.CharField(max_length=100)
    reminder = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)  # Add the is_online checkbox

    def __str__(self):
        return f"{self.module} - {self.day} - {self.time}"

class ClassSchedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.CharField(max_length=100)
    day = models.CharField(max_length=20)
    time = models.TimeField()
    venue = models.CharField(max_length=100)
    is_online = models.BooleanField(default=False)  # Add the is_online checkbox

    def __str__(self):
        return f"{self.module} - {self.day} - {self.time}"

class WellnessCheck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    mood = models.CharField(max_length=100)
    stress_level = models.CharField(max_length=100)
    tiredness_level = models.CharField(max_length=100, choices=[('Not tired', 'Not tired'), ('A little tired', 'A little tired'), ('Very tired', 'Very tired')])  # Add tiredness level
    notes = models.TextField(blank=True, null=True)  # Optional notes field

    def __str__(self):
        return f"Wellness Check for {self.user.username} on {self.date}"
    
    MOOD_CHOICES = [
    ('Happy', 'Happy'),
    ('Sad', 'Sad'),
    ('Neutral', 'Neutral'),
]

STRESS_LEVEL_CHOICES = [
    ('Low', 'Low'),
    ('Moderate', 'Moderate'),
    ('High', 'High'),
]

TIRENDESS_LEVEL_CHOICES = [
    ('Not tired', 'Not tired'),
    ('A little tired', 'A little tired'),
    ('Very tired', 'Very tired'),
]

