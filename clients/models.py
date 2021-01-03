from django.db import models


class Client(models.Model):
    class Meta:
        db_table = "clients"
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    first_name = models.CharField(blank=False, null=False, max_length=50, verbose_name="First Name")
    last_name = models.CharField(blank=False, null=False, max_length=50, verbose_name="Last Name")
    nick_name = models.CharField(blank=False, null=False, max_length=50, verbose_name="Nick Name")
    email = models.EmailField(blank=False, null=False, max_length=60, verbose_name="Email")
    password = models.CharField(blank=False, null=False, max_length=25, verbose_name="Password")
    address = models.CharField(blank=False, null=False, max_length=50, verbose_name="Street Address")
    city = models.CharField(blank=False, null=False, max_length=20, verbose_name="City")
    province = models.CharField(blank=False, null=False, max_length=20, verbose_name="Province / State")
    country = models.CharField(blank=False, null=False, max_length=40, verbose_name="Country")
    postal_code = models.CharField(blank=False, null=False, max_length=10, verbose_name="Postal / Zip Code")