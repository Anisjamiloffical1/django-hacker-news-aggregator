from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    points = models.IntegerField(default=0)
    author = models.CharField(max_length=255)
    comments = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    