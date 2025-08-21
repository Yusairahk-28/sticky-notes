from django.db import models


# Title and content of the note, max length of characters.
class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    # Returns title when called.
    def __str__(self):
        return self.title
