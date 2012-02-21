from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Submitter(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    url = models.URLField()
    
    def __unicode__(self):
        return self.name
    
class Idea(models.Model):
    submitter = models.ForeignKey(Submitter)
    title = models.CharField(max_length=128)
    slug = models.SlugField(blank=True)
    summary = models.CharField(max_length=512)
    desc = models.TextField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Idea, self).save(*args, **kwargs)


    def __unicode__(self):
        return self.title


class KVPairs(models.Model):
    k = models.CharField(max_length=128)
    v = models.CharField(max_length=1024)

    def __unicode__(self):
        return self.k

