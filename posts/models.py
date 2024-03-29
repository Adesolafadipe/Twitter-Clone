from django.db import models
from  cloudinary.models import CloudinaryField
class Post(models.Model):
    class Meta(object):
        db_table = 'post'
        
    name = models.CharField (
        'Name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
        )
    body = models.CharField (
        'body', blank=True, null=True, max_length=140, db_index=True
        )
    created_at = models.DateTimeField(
        'created DateTime', blank=True, auto_now_add=True
        )
    count= models.IntegerField(
        'count' ,blank=True,default=0
    )
    image =CloudinaryField(
        'image', blank=True, db_index=True 
    )