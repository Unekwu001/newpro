from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Schools(models.Model):
    name = models.CharField(max_length=20,unique=True)
    address = models.CharField(max_length=20,default="Null",null=True,blank=True)
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
    pic = CloudinaryField('image',default="Null")
    points= models.CharField(max_length=15,unique=False,default="Null")
    status = models.CharField(max_length=15,null=True,blank=True,default='unverified')
    date_joined = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    class Meta:
        db_table='agents'


class Lodges(models.Model):
    name = models.CharField(max_length=50,unique=False,default="Null")
    location = models.CharField(max_length=100,unique=False,default="Null")
    lodgetype = models.CharField(max_length=30,unique=False,default="Null")
    price = models.CharField(max_length=15,unique=False,default="Null")
    Tiled = models.CharField(max_length=15,unique=False,default="Null")
    light = models.CharField(max_length=15,unique=False,default="Null")
    fenced = models.CharField(max_length=15,unique=False,default="Null")
    water = models.CharField(max_length=15,unique=False,default="Null")
    status = models.CharField(max_length=15,unique=False,default="Null")
    region = models.CharField(max_length=15,unique=False,default="Null")
    agentid = models.CharField(max_length=15,unique=False,default="Null")
    date_uploaded = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='lodges'


class Lodgepics(models.Model):
    picname = CloudinaryField('image',default="Null")
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
    fullname = models.CharField(max_length=30,unique=False,default="Null",null=True,blank=True)
    phone = models.CharField(max_length=30,unique=False,default="Null",null=True,blank=True)
    religion = models.CharField(max_length=30,unique=False,default="Null")
    lodgerent = models.CharField(max_length=30,unique=False,default="Null")
    location = models.CharField(max_length=100,unique=False,default="Null")
    pic = CloudinaryField('image',default="Null")
    lodgetype = models.CharField(max_length=30,unique=False,default="Null")
    pricesharing = models.CharField(max_length=15,unique=False,default="Null")
    tiled = models.CharField(max_length=15,unique=False,default="Null")
    light = models.CharField(max_length=15,unique=False,default="Null")
    water = models.CharField(max_length=15,unique=False,default="Null")
    date_uploaded = models.DateTimeField(auto_now_add=True)
    pic1 = CloudinaryField('image',default="Null")
    pic2 = CloudinaryField('image',default="Null")
    pic3 = CloudinaryField('image',default="Null")

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


class Schedule_Inspection(models.Model):
    date_of_inspection = models.DateField(max_length=150, null=True,blank=True)
    timeof_inspection = models.CharField(max_length=150, null=True,blank=True)
    studentname = models.CharField(max_length=150, null=True,blank=True)
    studentphone = models.CharField(max_length=150, null=True,blank=True)
    studentemail = models.CharField(max_length=150, null=True,blank=True)
    lodgename = models.CharField(max_length=150, null=True,blank=True)
    lodgeid = models.CharField(max_length=150, null=True,blank=True)
    inspection_status = models.CharField(max_length=150, null=True,blank=True,default='inprogress')
    class Meta:
        db_table='schedule_inspection'

    

class Roomymatching_table(models.Model):
    owner_name = models.CharField(max_length=150, null=True,blank=True)
    owner_phone = models.CharField(max_length=150, null=True,blank=True)
    seeker_name = models.CharField(max_length=150, null=True,blank=True)
    seeker_phone = models.CharField(max_length=150, null=True,blank=True)
    date_ofmeeting = models.DateField(max_length=150, null=True,blank=True)
    time_ofmeeting = models.CharField(max_length=150, null=True,blank=True)
    match_status =  models.CharField(max_length=150, null=True,blank=True,default="inprogress")

    class Meta:
        db_table='roomymatching_table'




class Hosts(models.Model):
    schoolname = models.CharField(max_length=30,unique=False,default="Null")
    fullname = models.CharField(max_length=100,unique=False,default="Null",null=True,blank=True)
    phone = models.CharField(max_length=30,unique=False,default="Null",null=True,blank=True) 
    location = models.CharField(max_length=100,unique=False,default="Null")
    lodgetype = models.CharField(max_length=30,unique=False,default="Null")
    hostprice = models.CharField(max_length=15,unique=False,default="Null")
    tiled = models.CharField(max_length=15,unique=False,default="Null")
    light = models.CharField(max_length=15,unique=False,default="Null")
    water = models.CharField(max_length=15,unique=False,default="Null")
    bankname = models.CharField(max_length=100,unique=False,default="Null")
    accountnumber = models.CharField(max_length=100,unique=False,default="Null")
    accountname = models.CharField(max_length=100,unique=False,default="Null")
    pic1 = CloudinaryField('image',default="Null")
    pic2 = CloudinaryField('image',default="Null")
    pic3 = CloudinaryField('image',default="Null")
    date_uploaded = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table='hosts'