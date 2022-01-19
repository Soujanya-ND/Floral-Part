from django.db import models

# Create your models here.
class flower(models.Model):
 flower_id=models.IntegerField(primary_key=True)
 flower_name=models.TextField()
 color=models.CharField(max_length=60)
 price=models.IntegerField()
 flower_img=models.ImageField(upload_to='floral/static/img')
 def __str__(self):
     return self.flower_name
  
class services(models.Model):
 purpose_id=models.IntegerField(primary_key=True)
 flower_id=models.IntegerField()
 name_of_service=models.TextField()
 price=models.IntegerField()
 flower_name=models.TextField()
 services_img=models.ImageField(upload_to='floral/static/img')
 def __str__(self):
     return self.name_of_service

class employee(models.Model):
  employee_id=models.IntegerField(primary_key=True)
  emp_name=models.TextField()
  address=models.TextField()
  email=models.EmailField()
  phone_no=models.CharField(max_length=40)
  
  looksafter=models.ManyToManyField(flower)
  def __str__(self):
     return self.emp_name


class customer(models.Model):
 customer_id=models.AutoField(primary_key=True)
 cust_name=models.TextField()
 password=models.TextField()
 address=models.TextField()
 email=models.EmailField()
 phone_no=models.CharField(max_length=40)
 
 looksafter=models.ManyToManyField(services)
 def __str__(self):
     return self.cust_name
 

class looksafters(models.Model):
 flower_id=models.ForeignKey(flower,on_delete=models.CASCADE)
 employee_id=models.ForeignKey(employee,on_delete=models.CASCADE)

 class meta:
   unique_together=(('flower_id','employee_id'),)


class order(models.Model):
 flower_id=models.ForeignKey(flower,on_delete=models.CASCADE)
#  customer_id=models.ForeignKey(customer,on_delete=models.CASCADE)
 looksafter=models.ManyToManyField(customer)

 class meta:
   unique_together=(('flower_id','customer_id'),)
 

class uses(models.Model):
 purpose_id=models.ForeignKey(services,on_delete=models.CASCADE)
 customer_id=models.ForeignKey(customer,on_delete=models.CASCADE)

 class meta:
   unique_together=(('purpose_id','customer_id'),)

 def __str__(self): 
     return self.customer_id
 
 
