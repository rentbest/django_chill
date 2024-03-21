from django.contrib.auth.models import User
from django.db import models
from mptt.models import TreeForeignKey


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(
        'self', 
        related_name='children', 
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    
    
    class MPTTMeta:
        order_insertion_by = ['name']
    
    
class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    

class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='articles/')
    text = models.TextField(max_length=200)
    category = models.ForeignKey(
        Category,
        related_name='post',
        on_delete=models.SET_NULL,
        null=True
    )
    tags = models.ManyToManyField(Tag, related_name='post')
    create_at = models.DateTimeField(auto_now_add=True)