from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Snippet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default="")
    description = models.TextField(blank=True)
    snippet = models.TextField(blank=True)
    snippet_language = models.CharField(max_length=20, blank=True)
    slug = models.SlugField(blank=True)
    snippet_body = models.CharField(max_length=50000, blank=True)
    time = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.snippet_body = self.snippet.replace('\r', '').split('\n')
        super(Snippet, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)

