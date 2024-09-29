from django.db import models
from django.contrib.auth.models import User
# Create your models here.
CATAGORY = (
    ('STATIONARY','Stationary'),
    ('ELECTRONIC','Electronic'),
    ('FURNITURE','Furniture'),
)
class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    category = models.CharField(max_length=200,choices=CATAGORY,null=True)  # Corrected spelling
    quantity = models.PositiveIntegerField(null=True)  # Removed max_length

    def __str__(self):
        return f'{self.name}-{self.quantity}'
class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null = True)
    staff = models.ForeignKey(User,on_delete=models.CASCADE,null = True)
    order_quantity = models.PositiveBigIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        staff_username = self.staff.username if self.staff else "Unknown"
        return f'{self.product} ordered by "{staff_username}"'
