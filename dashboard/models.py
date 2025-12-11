from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class SalesData(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sales')
    date = models.DateField(default=timezone.now)
    quantity = models.IntegerField()
    revenue = models.DecimalField(max_digits=12, decimal_places=2)
    cost = models.DecimalField(max_digits=12, decimal_places=2)
    profit = models.DecimalField(max_digits=12, decimal_places=2)
    
    def save(self, *args, **kwargs):
        """Auto-calculate profit before saving"""
        self.profit = self.revenue - self.cost
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.product.name} - {self.date}"
    
    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Sales Data"
