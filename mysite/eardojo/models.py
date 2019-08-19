from django.db import models
from django.conf import settings

# Create your models here.

class Topic(models.Model):
    topic_title = models.CharField(max_length=100)
    topic_text = models.TextField()

    def __str__(self):
        return self.topic_title
        return self.topic_text
