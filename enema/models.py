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
    pic = models.FileField(null=True,blank=True,default='Null',upload_to='media/')
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
    picname = models.FileField(null=True,blank=True,default='Null',upload_to='media/')
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
    pic = models.FileField(null=True,blank=True,default='Null',upload_to='media/')
    lodgetype = models.CharField(max_length=30,unique=False,default="Null")
    pricesharing = models.CharField(max_length=15,unique=False,default="Null")
    tiled = models.CharField(max_length=15,unique=False,default="Null")
    light = models.CharField(max_length=15,unique=False,default="Null")
    water = models.CharField(max_length=15,unique=False,default="Null")
    date_uploaded = models.DateTimeField(auto_now_add=True)
    pic1 = models.FileField(null=True,blank=True,default='Null',upload_to='media/')
    pic2 = models.FileField(null=True,blank=True,default='Null',upload_to='media/')
    pic3 = models.FileField(null=True,blank=True,default='Null',upload_to='media/')

    class Meta:
        db_table='roomates'


class CustomerInfo(models.Model):
    fullname= models.CharField(max_length=150, null=True,blank=True)
    email= models.EmailField(null=True,blank=True)
    phonenumber = models.CharField(max_length=150,null=True,blank=True)
    amount = models.IntegerField(default=1000,null=True,blank=True)
    payfor = models.CharField(max_length=150, null=True,blank=True)
    class Meta:
        db_table='customer_infos'


class  Myadmin(models.Model):
    username= models.CharField(max_length=150, null=True,blank=True)
    pwd= models.CharField(max_length=150, null=True,blank=True)
    class Meta:
        db_table='myadmin'