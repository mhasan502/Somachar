from django.db import models


# News Model
class News(models.Model):
    """
    Model definition for News.
    """
    id = models.AutoField(primary_key=True)
    heading = models.TextField(max_length=100, unique=True, null=False)
    imagelink = models.CharField(max_length=255)
    newslink = models.CharField(max_length=255, null=False)
    details = models.TextField(null=False)
    papername = models.CharField(max_length=100, null=False)
    time = models.DateTimeField(auto_now_add=True, null=False)

    class Meta:
        """
        Meta definition for News.
        """
        verbose_name = 'News'

    def __str__(self):
        return str(self.heading)
