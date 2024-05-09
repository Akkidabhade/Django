from django.db import models
from django.utils import timezone

class CustomeManager(models.Manager):
    def get_customer_amount_range(self, r1, r2):
        return super().get_queryset().filter(amount__range=(r1, r2))
    def search(self, query):
        return super().get_queryset().filter(name__icontains=query)


class Cunsumer(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    name = models.CharField(max_length=30)
    phone = models.BigIntegerField()
    account_no = models.BigIntegerField()
    dob = models.DateTimeField()
    addr = models.CharField(max_length=50)
    email = models.EmailField()
    image = models.ImageField(upload_to="images/")
    amount = models.FloatField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    document = models.FileField(upload_to="documents/")


    objects = models.Manager()
    customers = CustomeManager()   

class Meta:
        ordering = ('-dob',)  

def __str__(self):
        return self.name

