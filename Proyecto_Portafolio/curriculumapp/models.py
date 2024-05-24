# curriculumapp/models.py
from django.db import models
from django.contrib.auth.models import User

class Curriculum(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    education = models.TextField(max_length=1000)
    experience = models.TextField()
    skills = models.TextField()

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = models.ImageField(upload_to='avatars/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
