from django.db import models


class Category(models.Model):
    parent = models.ForeignKey('self',blank=True,null=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description=models.TextField(blank=True)
    avatar = models.ImageField(blank=True, upload_to='categories')
    is_enable=models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    title =models.CharField(max_length=50)
    description=models.TextField(blank=True)
    avatar = models.ImageField(blank=True, upload_to='products/')
    is_enable=models.BooleanField(default=True)
    categories=models.ManyToManyField('Category',blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'products'
        verbose_name = 'product'
        verbose_name_plural = 'products'


class File(models.Model):
    product = models.ForeignKey('Product',on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
   # file= models.FieldFile(upload_to='file')
    file= models.FileField(upload_to='file')
    is_enable=models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'files'
        verbose_name = 'file'
        verbose_name_plural = 'files'
 


