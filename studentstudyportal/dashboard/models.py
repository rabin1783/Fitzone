from turtle import title
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Notes(models.Model):
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    

    class Meta:
        verbose_name = "notes",
        verbose_name_plural = "notes"

    def __str__(self):
        return self.title


class Homework(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)


    def __str__(self):
        return self.title

class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class AppUser(models.Model):

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15)
    dob = models.DateField()
    password = models.CharField(max_length=100)
    password1 = models.CharField(max_length=100)
    profile_pic = models.FileField()
    address = models.CharField(max_length=200)
    verification_code = models.CharField(max_length=8)
    is_verified = models.BooleanField(default=False)
    is_removed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=0)
    update_at = models.DateTimeField(null=True)
    removed_at = models.DateTimeField(null=True) 
    
    class Meta:
        db_table = "app_users"

    def __str__(self):
        return self.first_name


class Step(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        
        self.cover.delete()
        super().delete(*args, **kwargs)