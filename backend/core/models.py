from django.db import models

# Create your models here.
class MusicFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='CueNavi/')

    def __str__(self):
        return self.title
