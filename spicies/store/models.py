from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string

from django.urls import reverse
# Create your models here.
from django.conf import settings



class Category(models.Model):
    name =models.CharField(max_length=255,db_index=True)
    slug=models.SlugField(max_length=255,unique=True,blank=True)

    class Meta:
        verbose_name_plural= 'Categories'

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("store:categories",args=[self.slug])
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager,self).get_queryset().filter(isactive=True)

class Product(models.Model):
    category = models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)
    created_by=models.ForeignKey(settings.AUTH_USER_MODEL,related_name="product_creator",on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    auther=models.CharField(max_length=255)
    describtion=models.TextField(blank=True)
    img=models.ImageField(upload_to='images/')
    slug=models.SlugField(max_length=255,unique=True, blank=True)
    
    price=models.DecimalField(max_digits=5,decimal_places=2)
    afterdiscont=models.DecimalField(max_digits=5,decimal_places=2)
    
    instock=models.BooleanField(default=True)
    isactive=models.BooleanField(default=True)

    whight=models.DecimalField(max_digits=10,decimal_places=5)

    created=models.TimeField(auto_now_add=True)
    updated=models.TimeField(auto_now=True)
    objects=models.Manager()
    products=ProductManager()

    class Meta:
        verbose_name_plural= 'Products'
        ordering=('-created',)


    def __str__(self):
        return self.title

    def get_prod_url(self):
        return reverse("store:prod_details",args=[self.slug])
    

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_str = "%s %s" % (self.title, self.category.name) 
            self.slug = slugify( get_random_string(8,'slug_str') )
        super(Product, self).save(*args, **kwargs)

    def discountprecent(self):
        return round(((self.price - self.afterdiscont)/self.price)*100)


    