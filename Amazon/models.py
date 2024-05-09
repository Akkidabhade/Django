from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class CustomeManager(models.Manager):
    def get_student_percentage_range(self, r1, r2):
        return super().get_queryset().filter(percentage__range=(r1, r2))
    def search(self, query):
        return super().get_queryset().filter(name__icontains=query)
    


class StudentProfile(models.Model):
    name = models.CharField(max_length=30)
    educ = models.CharField(max_length=30)
    email = models.EmailField()
    image = models.ImageField(upload_to="images/")
    phone = models.BigIntegerField()
    dob = models.DateTimeField(default=timezone.now)
    addr = models.CharField(max_length=50)
    percentage = models.BigIntegerField()

    objects = models.Manager()
    students = CustomeManager()    

    class Meta:
        ordering = ('-dob',)  

    def __str__(self):
        return self.name  

class Product(models.Model):
    pname = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to="media/")

def __str__(self):
    return self.pname

class CartItems(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date =models.DateTimeField(auto_now_add=True)
 
def __str__(self):
    return f'{self.quantity} * {self.product.pname}'