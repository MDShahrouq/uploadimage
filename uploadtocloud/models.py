from django.db import models
import time
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.core.validators import RegexValidator
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
import random
from random import randint

owner = models.ForeignKey('auth.User', related_name='register')
highlighted = models.TextField()

class Uploadtoimage(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    c_type = models.TextField(blank=True,default='',null=True)
    photo = models.ImageField(upload_to="/projectimg",null=True, blank=True)
    img_name = models.TextField(null=True,blank=True,default='')
    img_type = models.TextField(null=True,blank=True,default='')
    
    class Meta:
        ordering = ('created',)
