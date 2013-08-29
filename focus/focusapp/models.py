from django.db import models

# Create your models here.

class Person(models.Model):
    kbid = models.CharField(max_length=40, primary_key=True)
    name = models.CharField(max_length=40)
    number = models.CharField(max_length=20)
    email = models.CharField(max_length=120)
    skype = models.CharField(max_length=120, blank=True, null=True)
    pic = models.CharField(max_length=512)

    def __unicode__(self):
        return self.name
