from django.db import models

# Create your models here.
class Schools(models.Model):
    name = models.CharField(max_length=20,unique=True)
    class Meta:
        db_table='schools'


class Agents(models.Model):
    name = models.CharField(max_length=100,unique=False,default="Null")
    email = models.CharField(max_length=100,unique=True,default="Null")
    pwd = models.CharField(max_length=100,unique=False,default="Null")
    phone = models.CharField(max_length=15,unique=False,default="Null")
    address = models.CharField(max_length=230,unique=False,default="Null")
    id_type = models.CharField(max_length=30,unique=False,default="Null")
    id_numb = models.CharField(max_length=30,unique=False,default="Null")
    pic = models.ImageField(null=True,blank=True,upload_to="media")
    points= models.CharField(max_length=15,unique=False,default="Null")
    class Meta:
        db_table='agents'


class Lodges(models.Model):
    name = models.CharField(max_length=50,unique=False,default="Null")
    location = models.CharField(max_length=100,unique=False,default="Null")
    lodgetype = models.CharField(max_length=30,unique=False,default="Null")
    price = models.CharField(max_length=15,unique=False,default="Null")
    Tiled = models.CharField(max_length=15,unique=False,default="Null")
    light = models.CharField(max_length=15,unique=False,default="Null")
    water = models.CharField(max_length=15,unique=False,default="Null")
    status = models.CharField(max_length=15,unique=False,default="Null")
    region = models.CharField(max_length=15,unique=False,default="Null")
    agentid = models.CharField(max_length=15,unique=False,default="Null")
    date_uploaded = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='lodges'


class Lodgepics(models.Model):
    picname = models.ImageField(max_length=100,null=True,blank=True)
    lodgeid = models.ForeignKey(Lodges,on_delete=models.CASCADE)
    agentid = models.CharField(max_length=15,unique=False,default="Null")
    sn=models.IntegerField(null=True,blank=True)
    class Meta:
        db_table='lodgepics'


class Locations(models.Model):
    location = models.CharField(max_length=100,unique=False,default="Null")
    school = models.CharField(max_length=30,unique=False,default="Null")
    class Meta:
        db_table='locations'
    

class Roomates(models.Model):
    schoolname = models.CharField(max_length=30,unique=False,default="Null")
    phone = models.CharField(max_length=30,unique=False,default="Null",null=True,blank=True)
    religion = models.CharField(max_length=30,unique=False,default="Null")
    lodgerent = models.CharField(max_length=30,unique=False,default="Null")
    location = models.CharField(max_length=100,unique=False,default="Null")
    pic = models.ImageField(max_length=100,unique=False,default="Null",null=True,blank=True,upload_to="media")
    lodgetype = models.CharField(max_length=30,unique=False,default="Null")
    pricesharing = models.CharField(max_length=15,unique=False,default="Null")
    tiled = models.CharField(max_length=15,unique=False,default="Null")
    light = models.CharField(max_length=15,unique=False,default="Null")
    water = models.CharField(max_length=15,unique=False,default="Null")
    date_uploaded = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='roomates'
