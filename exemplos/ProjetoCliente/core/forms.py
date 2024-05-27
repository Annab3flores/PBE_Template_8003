from django import forms
from .models import Customer, Address, Order
from django.forms import inlineformset_factory

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'neighborhood', 'city', 'state', 'zip_code', 'latitude', 'longitude', 'customer']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product_name', 'quantity', 'price']

AddressFormSet = inlineformset_factory(Customer, Address, form=AddressForm, extra=1)
OrderFormSet = inlineformset_factory(Customer, Order, form=OrderForm, extra=1)