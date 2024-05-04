from django.db import models
from django.contrib.auth.models import AbstractUser

class Paragraph(models.Model):
    # Auto-incremented primary key field
    id = models.BigAutoField(primary_key=True)

    # Text content of the paragraph
    content = models.TextField()

    # String representation of the Paragraph object
    def __str__(self):
        return f"Paragraph {self.id}"

class Word(models.Model):
    word = models.CharField(max_length=50)
    paragraph = models.ForeignKey(Paragraph, related_name='words', on_delete=models.CASCADE)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    dob = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email
