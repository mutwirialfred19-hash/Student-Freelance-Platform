from django.contrib.auth.models import AbstractUser
from django.db import models
import re

class User(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('client', 'Client'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    email_verified = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def is_student(self):
        return self.role == 'student'

    def is_client(self):
        return self.role == 'client'

    def is_kca_email(self):
        pattern = r'^\d+@students\.kcau\.ac\.ke$'
        return bool(re.match(pattern, self.email))
