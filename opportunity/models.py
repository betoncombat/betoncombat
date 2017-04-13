from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class OpportunityItem(models.Model):

    content = HTMLField()
    image =  models.ImageField(upload_to = 'media/opportunity/', blank=True)
    order = models.IntegerField()

    def __unicode__(self):

        return self.content