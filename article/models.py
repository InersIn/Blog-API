from django.db import models
from django.utils import timezone
# Create your models here.
class Article(models.Model):
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=(1024*4))
    created = models.DateField(auto_now=False, auto_now_add=False)
    modified = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now().replace(day=10)
        self.modified = timezone.now().replace(day=10)
        return super(Article, self).save(*args, **kwargs)