from django.db import models
from django.conf import settings


# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Tags'
        ordering = ['title']


class Plan(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    limit = models.IntegerField(default=10)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField()
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=14)  # Example : (98) 911 111 1111
    birth_date = models.DateField(null=True, blank=True)
    join_date = models.DateTimeField(auto_created=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        ordering = ['user']


class Mentor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=14)  # Example : (98) 911 111 1111
    birth_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan = models.OneToOneField(Plan, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        ordering = ['first_name', 'last_name']
