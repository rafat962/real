from django.db import models

# Create your models here.



class Main(models.Model):
    flat_img = models.ImageField(null=True,blank=True)
    flat_name = models.TextField(max_length=200,null=True,blank=True)
    flat_dic = models.TextField(max_length=200,null=True,blank=True)
    num_bed = models.IntegerField(max_length=4,null=True,blank=True)
    num_path = models.IntegerField(max_length=4,null=True,blank=True)
    num_sq = models.IntegerField(max_length=20,null=True,blank=True)
    sub_img = models.ImageField(null=True,blank=True)
    iid = models.IntegerField(max_length=200,null=True,blank=True)
    def __str__(self):
        return self.flat_name

class Flat(models.Model):
    flat_price = models.TextField(max_length=100,null=True,blank=True)
    detail_loac = models.TextField(max_length=100,null=True,blank=True)
    flat_loac = models.TextField(max_length=100,null=True,blank=True)
    ph_1 = models.ImageField(null=True,blank=True)
    ph_2 = models.ImageField(null=True,blank=True)
    ph_3 = models.ImageField(null=True,blank=True)
    ph_4 = models.ImageField(null=True,blank=True)
    ph_5 = models.ImageField(null=True,blank=True)
    iid = models.IntegerField(max_length=200,null=True,blank=True)
    x1 = models.FloatField(null=True,blank=True)
    y1 = models.FloatField(null=True,blank=True)
    x2 = models.FloatField(null=True,blank=True)
    y2 = models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.flat_price

