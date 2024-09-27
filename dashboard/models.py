from django.db import models

# Create your models here.
CATAGORY = (
    ('STATIONARY','Stationary'),
    ('ELECTRONIC','Electronic'),
    ('FURNITURE','Furniture'),
)
class product(models.Model):
    name = models.CharField(max_length=200,null=True)
    category = models.CharField(max_length=200,choices=CATAGORY,null=True)  # Corrected spelling
    quantity = models.PositiveIntegerField(max_length=200,null=True)  # Removed max_length

    def __str__(self):
        return f'{self.name}-{self.quantity}'
