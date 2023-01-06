from django.db import models
from django.template.defaultfilters import slugify 
from django.core.validators import MinLengthValidator
from django.core.validators import MaxValueValidator, MinValueValidator 
# Create your models here.

class TagModel(models.Model):
    catagory=models.CharField(max_length=300)
    def __str__(self):
        return self.catagory
    
class EmailModel(models.Model):
    email=models.EmailField(max_length=300)
    def __str__(self):
        return self.email

class ContentModel(models.Model):
    
    title = models.CharField(max_length=300,unique=True)
    slug = models.SlugField(default="",null=False,unique=True)
    article=models.TextField()
    tag=models.ForeignKey(TagModel,on_delete=models.CASCADE,blank=True,null=True,related_name='content')

    
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.slug