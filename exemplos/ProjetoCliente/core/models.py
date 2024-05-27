from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Address(models.Model):
    street = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=100, null=True, blank=True)  # Novo campo
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)  # Novo campo
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)  # Novo campo
    customer = models.ForeignKey(Customer, related_name='addresses', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.street}, {self.city}"

class Order(models.Model):
    product_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.id} - {self.customer.name}"
