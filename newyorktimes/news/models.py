from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('details_news', kwargs={'pk': self.pk})
