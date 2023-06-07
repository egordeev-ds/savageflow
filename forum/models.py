from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    content_html = models.TextField(blank=True, null=True)  # Добавленное поле для хранения отформатированного текста
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    
class Answer(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='answer_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Answer to {self.post.title}"