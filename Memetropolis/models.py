from django.db import models
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey('auth.User')
    category = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(
            blank=True, null=True)
    def approved_comments(self):
    return self.comments.filter(approved_comment=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.category

class Comment(models.Model):
    post = models.ForeignKey('Memetropolis.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
# Create your models here.
