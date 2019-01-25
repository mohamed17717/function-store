from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save

import datetime

from random import choice
def randint(n=8):
    return ''.join( [ str(choice([0,1,2,3,4,5,6,7,8,9])) for i in range(n)] )

# Create your models here.
class Function(models.Model):
    """This just handle function data in db"""

    name    = models.CharField(max_length=70)
    content = models.TextField()
    comment = models.TextField()
    tags    = models.CharField(max_length=100)
    slug    = models.CharField(unique= True, blank=True, max_length=100)
    created = models.DateTimeField(auto_now=False, default= datetime.datetime.now)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Function'
        verbose_name_plural = 'Functions'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify( '%s-%s' % ( self.name, randint() ) )
        return super(Function, self).save(*args, **kwargs)

class Tag(models.Model):
    name      = models.CharField(unique=True, max_length=70)
    functions = models.ManyToManyField(Function, blank=True)

    def __str__(self):
        return self.name

from django.core.exceptions import ObjectDoesNotExist
def get_object(Class, **kwargs):
    try:
        return Class.objects.get(**kwargs)
    except ObjectDoesNotExist:
        return None

def attach_func_to_tag(sender, instance, created, **kwargs):
    # if created:
    tags = instance.tags.split(' ')
    for tag in tags:
        ## chk if tag already exist: just add the function 
        ## else create the tag then add the function

        t = get_object(Tag, name= tag)
        if not t:
            t = Tag.objects.create(name= tag)
        t.functions.add(instance)

post_save.connect(attach_func_to_tag, sender=Function)