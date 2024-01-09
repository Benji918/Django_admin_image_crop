from django.db import models
from django.utils.html import mark_safe
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)

    @property
    def thumbnail_preview(self):
        if self.thumbnail:
            _thumbnail = get_thumbnail(self.thumbnail,
                                       '50x50',
                                       upscale=False,
                                       crop=False,
                                       quality=100)
            return format_html(
                '<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""
