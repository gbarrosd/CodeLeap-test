from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    username = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_datetime', )

    def __str__(self):
        return self.title
    
