from django.db import models
from ecommerceAPP.models import Product
# Create your models here.
class Cart(models.Model):
    cart_id=models.CharField(max_length=200,blank=True)
    date=models.DateField(auto_now_add=True)
    class Meta:
        db_table='Cart'
        ordering=['date']
    def __str__(self):
        return '{}'.format(self.cart_id)
class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)
    class Meta:
        db_table='Cart Item'
    def subtotal(self):
        return self.product.price * self.quantity
    def __str__(self):
        return '{}'.format(self.product)