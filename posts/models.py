# from users.models import User
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, null=False)
    content = models.CharField(max_length=128, null=False)
    created_ad = models.DateTimeField

    def __str__(self):
        return f"Post of user: {self.user}, {self.title}, {self.content}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    content = models.CharField(max_length=120)
    created_ad = models.DateTimeField(null=False)

    def __str__(self):
        return f"Comment od: {self.user}, {self.post}, {self.content}"
