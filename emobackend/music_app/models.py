from django.db import models

class Song(models.Model):
    EMOTIONS = [
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('angry', 'Angry'),
        ('neutral', 'Neutral')
    ]
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    url = models.URLField()
    emotion = models.CharField(max_length=10, choices=EMOTIONS)

    def __str__(self):
        return self.title
