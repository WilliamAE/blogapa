# posts/models.py
from django.conf import settings
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)#creacion de manera automatica del registro
    updated_at = models.DateTimeField(auto_now=True)#actualizacion de manera automatica del registro

    def __str__(self):
        return self.title


