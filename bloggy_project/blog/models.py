from django.db import models

# Create your models here.
class Post(models.Model): # defines the database table
    # This class creates each of these fields
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    tag = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    views = models.IntegerField(default=0)

    '''def __unicode__(self):
        return str(self.id) + " / " + str(self.created_at) + " / " + self.title + " / " + self.content + "\n"'''

    def __unicode__(self):
        return self.title