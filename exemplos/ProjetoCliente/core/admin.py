from django.contrib import admin
from .models import Customer, Address, Order

# Register your models here.
admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Order)