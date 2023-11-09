from django.db import models

from taggit.managers import TaggableManager




class Product(models.Model):
    name = models.CharField(max_length=225,default=None)
    slug=models.SlugField(max_length=225, unique=True)
    subcategory=models.ForeignKey('Product', on_delete=models.CASCADE, blank=True, null=True)
    totalprice=models.IntegerField()
    saleprice = models.IntegerField()
    discount = models.IntegerField(default=None)
    title=models.CharField(max_length=225)
    image= models.ImageField(blank=True, upload_to ='static/img')
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title




