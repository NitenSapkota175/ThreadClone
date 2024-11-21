from django.db import models
from users.models import CustomUser


class Post(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="tweets"
    )
    content = models.TextField(max_length=280)
    img = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies"
    )

    def __str__(self):
        return f"Tweet by {self.user.email} on {self.created_at}"


class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} liked post {self.post.id}"


class Repost(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="reposts"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reposted_by")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} reposted post {self.post.id}"
