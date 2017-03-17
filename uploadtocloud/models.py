from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Uploadtocloud_images(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    #v_id = models.CharField(max_length=100,null=True, blank=True,default='')
    photo = models.ImageField(upload_to="/projectimg",null=True, blank=True)
    link=models.TextField(blank=True,default='')
    img_name = models.TextField(null=True,blank=True,default='')
    img_type = models.TextField(null=True,blank=True,default='')
    
   # photo = models.ImageField(upload_to="projectimg/",storage=fs, null=True, blank=True)
    
    
    class Meta:
        ordering = ('created',)