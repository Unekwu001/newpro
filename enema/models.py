from django.db import models
from config.settings import client

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

    def __str__(self):
        return str(self.studentname)

    def save(self,*args,**kwargs):
        message = client.messages.create(
            body=f'Congratulations {self.studentname} ! You have been scheduled to inspect {self.lodgename} as follows: \n Date of inspection: {doi} \n Time of inspection: {toi} \n Meeting venue: Kitchen 54 Tammah. \n\n Have a wonderful day ahead. \n Jemimah Adiburmi\n Head of people.\n Enema Corporations.',
            from_='+12182281796',
            to={self.studentphone}
        )
        print(message.sid)
        return super().save(*args,**kwargs)
