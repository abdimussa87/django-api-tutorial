from django.db import models

# Create your models here.

class Note(models.Model):
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return the first 50 characters of the body
        return self.body[:50]

    class Meta:
        # order by the most recently updated
        ordering = ['-updated']