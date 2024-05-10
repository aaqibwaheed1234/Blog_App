from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth import get_user_model
User = get_user_model()

class Post(models.Model):
    user=models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, null=True, blank=True)
    title=models.CharField(max_length=55)
    slug=models.SlugField(max_length=55)
    intro=models.CharField(max_length=55)
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='uploads/', blank=True,null=True)
    class Meta:
        ordering=('-created_at',)


class Comment(models.Model):
    post=models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user=models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=255)
    email=models.EmailField()
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('users_app.Post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'post']


class CustomUser(AbstractUser):
    picture = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'
        unique_together = [['username']]

CustomUser._meta.get_field('groups').remote_field.related_name = 'customuser_groups'
CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'customuser_user_permissions'