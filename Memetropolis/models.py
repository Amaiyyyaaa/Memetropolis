from django.db import models
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey('auth.User')
    category = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.category
# Create your models here.
