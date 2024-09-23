from django.db import models
from django.contrib.auth.models import User

STATUS= (
    (0,'Draft'),
    (1,'publish')
)
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=300,unique=True)
    slug=models.SlugField(max_length=300,unique=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_post')
    content=models.TextField()
    updated_on=models.DateTimeField(auto_now=True)
    created_on=models.DateTimeField(auto_now_add=True)
    status=models.IntegerField(choices=STATUS,default=0) #default=0 : drafted one

class meta:
    ordering=['-created_on']

def __str__(self):
    return self.title

