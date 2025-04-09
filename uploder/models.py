from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/',null= True,blank=True)
    files = models.FileField(upload_to='files/', null = True,blank=True)
    addDate = models.DateField(auto_now_add=True)

    def __str__(self):
        user_name = self.user.username if self.user else "Unknown User"
        file_name = self.files.name if self.files else "No File"
        return f"{user_name} - {file_name}"



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', default='default.jpg')
    location = models.CharField(max_length=100, blank=True, null=True)
    skills = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username
