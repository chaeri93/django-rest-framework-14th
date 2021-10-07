from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=40, blank=True)
    introduction = models.TextField(blank=True)
    image = models.ImageField()

    def __str__(self):
        return self.nickname


class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True)
    location = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    like_num = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class File(models.Model):
    post = models.ForeignKey(Post, blank=False, null=False, on_delete=models.CASCADE)
    content = models.FileField(upload_to="media")


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} commented {} post'.format(self.writer, self.post.author)

class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE)
    following = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return '{} -> {}'.format(self.follower.nickname, self.following.nickname)

