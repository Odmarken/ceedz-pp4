from django.db import models
from django.contrib.auth.models import User
from blog.models import Post

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} likes {self.post.title}"
