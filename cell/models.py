from django.db import models

# Create your models here.
class User(models.Model):
    userid = models.AutoField(primary_key=True,db_index=True)
    name = models.CharField(max_length = 140)
    phone = models.CharField(max_length = 12)
    email = models.EmailField(db_index=True)
    password = models.CharField( max_length=128)
    city = models.CharField(max_length = 12)
    campaign_name = models.CharField(max_length = 30)
    usertype = models.IntegerField(db_index=True)
    
    def __str__(self):
        return self.name


class Offer(models.Model):
    offerid = models.AutoField(primary_key=True,db_index=True)
    packageid= models.IntegerField()
    network = models.CharField(max_length = 140)
    packageDesc = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.packageDesc

class SimCard(models.Model):
    simid = models.AutoField(primary_key=True)
    serial = models.CharField(max_length = 20, db_index=True)
    userid = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    offerid = models.ForeignKey(Offer,on_delete=models.SET_NULL,null=True,blank=True)
    
    passport = models.CharField(max_length = 12,db_index=True,default='',blank=True)
    nationality = models.CharField(max_length = 140,default='',blank=True)
    phone = models.CharField(max_length = 12, help_text="Enter phone number..")
    original_balance = models.DecimalField(max_digits=10,decimal_places=2)
    current_balance = models.DecimalField(max_digits=10,decimal_places=2)
    activated = models.BooleanField(default=False,blank=True)
    time_activate = models.DateTimeField(null=True,blank=True)
    fingerprint = models.BinaryField(null=True,blank=True)
    time_enrol = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.phone