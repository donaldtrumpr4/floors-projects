from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    author = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    datetime = models.DateTimeField(u'Дата публикации', default=timezone.now)
    content = models.TextField(max_length=10000)

    def __unicode__(self):
        return self.title

    def get_url(self):
        return str(self.id)

