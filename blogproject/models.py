from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
