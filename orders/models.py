from django.db import models
from clients.models import Client
from products.models import Product


class Order(models.Model):
    class Meta:
        db_table = "orders"
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    client = models.ForeignKey(Client, blank=False, null=True, verbose_name="Good", on_delete=models.CASCADE)
    date = models.DateTimeField(blank=False, null=False, verbose_name="Order Date / Time")
    payment_method = models.CharField(blank=False, null=False, max_length=20, verbose_name="Payment method")
    delivery_method = models.CharField(blank=False, null=False, max_length=20, verbose_name="Payment method")
    delivery_date = models.DateTimeField(blank=False, null=False, verbose_name="Delivery Date")
    total_price = models.FloatField(blank=False, null=False, verbose_name="Sub total")


class Cart(models.Model):
    class Meta:
        db_table = "carts"
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    order = models.ForeignKey(Order, blank=False, null=True, verbose_name="Order", on_delete=models.CASCADE)
    date = models.DateTimeField(blank=False, null=False, verbose_name="Cart Date / Time Created")
    item_price = models.FloatField(blank=False, null=False, verbose_name="Item Price")
    product_quantity = models.IntegerField(blank=False, null=False, verbose_name="Product(s) Count")
    sub_total = models.FloatField(blank=False, null=False, verbose_name="Sub total")
    product = models.ForeignKey(Product,blank=False, null=True, verbose_name="Good", on_delete=models.CASCADE)