from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    username = models.CharField(max_length=20)
    birthdate = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")
    post = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=255)

class Engagement(models.Model):
    like = models.PositiveIntegerField()
    comments = models.PositiveIntegerField()
    upvote = models.PositiveIntegerField()
    downvote = models.PositiveIntegerField()
    save = models.ManyToManyField(Post, blank=True, related_name="engagement")
    award = models.ForeignKey(User, on_delete=models.CASCADE, related_name="engagement")

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="posts")
    comment = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)

