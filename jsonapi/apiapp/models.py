from django.db import models


class blogData(models.Model):
    title = models.CharField(max_length=80, null=False)
    body = models.CharField(max_length=1000, null=False)
    author = models.CharField(max_length=20, null=False)

    def __str__(self):
        return '{}'.format(self.title)
