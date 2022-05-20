from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_ad = models.DateTimeField(auto_now_add=True)
    upgrade_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)