from django.db import models

class Blog(models.Model):
    author = models.CharField(max_length=50, blank=True, null=True)
    content = models.CharField(max_length=500, blank=False, null=False)

    def __str__(self):
        return self.author
