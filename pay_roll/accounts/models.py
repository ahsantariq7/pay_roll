from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


phone_validator = RegexValidator(r"^(\+?\d{0,4})?\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{4}\)?)?$", "The phone number provided is invalid")


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=200, validators=[phone_validator], unique=True)
    is_business=models.BooleanField("Business/Company(Business Account Type)",default=False)
    is_accountant=models.BooleanField("Accountant Account Type",default=False)

    REQUIRED_FIELDS = ["phone", "email","is_business","is_accountant"]

class Pay1(models.Model):
    pay_frequency = models.CharField(max_length=200)
    
    def __str__(self):
        return self.pay_frequency

class Data_Range1(models.Model):
    Start_Date = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.Start_Date

class Data_Range2(models.Model):
    End_Date = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.End_Date


class Period_Number(models.Model):
    period_number = models.CharField(max_length=200)
    
    def __str__(self):
        return self.period_number



class Create_Business(models.Model):
 
    # fields of the model
    business_name = models.CharField(max_length = 200)
    street1=models.CharField(max_length = 200)
    street2=models.CharField(max_length = 200)
    city=models.CharField(max_length = 200)
    postal_code=models.CharField(max_length = 200)
    parish=models.CharField(max_length = 200)
    country=models.CharField(max_length = 200,default='Jamaica')
    Tax_Registration_No=models.CharField(max_length = 200)
    National_Insurance_Scheme_Number=models.CharField(max_length = 200)
    Business_Start_Date= models.DateTimeField()
    pay=models.ForeignKey(Pay1,on_delete=models.CASCADE)
    Date1=models.ForeignKey(Data_Range1,on_delete=models.CASCADE)
    Date2=models.ForeignKey(Data_Range2,on_delete=models.CASCADE)
    Period=models.ForeignKey(Period_Number,on_delete=models.CASCADE)
    Name_On_Account=models.CharField(max_length=200)
    Bank_Name=models.CharField(max_length=200)
    Branch=models.CharField(max_length=200)
    Account_Number=models.CharField(max_length=200)
    Account_Type=models.CharField(max_length=200)
    
 
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.business_name
