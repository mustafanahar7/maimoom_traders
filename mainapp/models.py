from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .manager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=15)
    profile_img = models.FileField(upload_to='profiles' , default='profiles/default-profile.png', null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    
class ProductInventory(models.Model):
    product_code = models.CharField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=70)
    first_purchase_date = models.DateField(null=True,default=None)
    last_purchase_date = models.DateField(null=True,default=None)
    product_category = models.CharField(max_length=60,null=True , default=None)
    product_description = models.TextField(null=True,default=None)
    quantity = models.IntegerField()
    product_image = models.FileField(upload_to='products/')
    cost_sqft = models.FloatField()
    selling_price_sqft = models.FloatField()
    total_amount_sqft = models.FloatField()
    godown_name = models.CharField(max_length=70 , default='Main')
    qty_sqft = models.FloatField(null=True , default=None)
    
    
    
class salesCustomerData(models.Model):
    
    sales_product =models.ForeignKey("mainapp.ProductInventory", on_delete=models.PROTECT)
    
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    customer_address = models.TextField()
    customer_phone_number = models.CharField(max_length=15)
    sales_date = models.DateField(auto_now=True)
    qty_in_sqft = models.FloatField()
    sale_price_sqft = models.FloatField()
    discount = models.FloatField(default=0,null=True)
    total_sale_amount = models.FloatField()
    
    
    
class customers_order_from_website(models.Model):
    order_number = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50,default=None , null=True)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15)
    address = models.TextField()
    pin_code = models.CharField(max_length=10)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)
    payment_id = models.CharField(max_length=100,default=None , null=True)
    order_id = models.CharField(max_length=100,default=None , null=True)
    
class website_orderItems(models.Model):
    order_number = models.ForeignKey("mainapp.customers_order_from_website", on_delete=models.PROTECT)
    product_code = models.ForeignKey("mainapp.ProductInventory",on_delete=models.PROTECT)
    selling_price = models.FloatField()
    qty = models.FloatField()
    gross_amount = models.FloatField()
    
    
    
class Queryform(models.Model):
    query_date = models.DateField(auto_now=True)
    name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=14)
    message = models.TextField()    
    
     