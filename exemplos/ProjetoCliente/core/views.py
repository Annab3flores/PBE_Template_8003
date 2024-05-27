from rest_framework import generics
from .models import Customer, Address, Order
from .serializers import CustomerSerializer, AddressSerializer, OrderSerializer

from django.shortcuts import render, get_object_or_404, redirect
from .forms import CustomerForm, AddressForm, OrderForm,  AddressFormSet, OrderFormSet

import folium 

from geopy.geocoders import Nominatim

import json

# Views para API
class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
#Views para o app Web

def index(request):
    return render(request, 'core/index.html')

# Customer Views
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'core/customer_list.html', {'customers': customers})

def customer_detail(request, id):
    customer = get_object_or_404(Customer, id=id)
    return render(request, 'core/customer_detail.html', {'customer': customer})

def customer_detail_with_details(request, id):
    customer = get_object_or_404(Customer, id=id)
    return render(request, 'core/customer_detail_with_details.html', {'customer': customer})

#####################################################################
def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer-list')
    else:
        form = CustomerForm()
    return render(request, 'core/customer_form.html', {'form': form})
######################################################################

def create_customer(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        address_formset = AddressFormSet(request.POST, prefix='addresses')
        order_formset = OrderFormSet(request.POST, prefix='orders')

        if customer_form.is_valid() and address_formset.is_valid() and order_formset.is_valid():
            customer = customer_form.save()
            address_formset.instance = customer
            address_formset.save()
            order_formset.instance = customer
            order_formset.save()
            return redirect('customer_detail', pk=customer.pk)
    else:
        customer_form = CustomerForm()
        address_formset = AddressFormSet(prefix='addresses')
        order_formset = OrderFormSet(prefix='orders')

    return render(request, 'core/create_customer.html', {
        'customer_form': customer_form,
        'address_formset': address_formset,
        'order_formset': order_formset,
    })

def customer_update(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer-list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'core/customer_form.html', {'form': form})

def customer_delete(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer-list')
    return render(request, 'core/customer_confirm_delete.html', {'customer': customer})

def customer_detail_with_map(request, id):
    customer = get_object_or_404(Customer, id=id)
    addresses = customer.addresses.all()

    # Create a map centered at the first address (if exists)
    if addresses:
        first_address = addresses[0]
        map_center = [first_address.latitude, first_address.longitude]
    else:
        map_center = [0, 0]  # Default center if no addresses

    m = folium.Map(location=map_center, zoom_start=13)

    # Add markers for each address
    for address in addresses:
        if address.latitude and address.longitude:
            folium.Marker(
                [address.latitude, address.longitude],
                popup=f"{address.street}, {address.city}",
                tooltip=address.neighborhood
            ).add_to(m)

    # Render the map as HTML
    map_html = m._repr_html_()

    return render(request, 'core/customer_detail_with_map.html', {'customer': customer, 'map_html': map_html})

# Address Views
def address_list(request):
    addresses = Address.objects.all()
    return render(request, 'core/address_list.html', {'addresses': addresses})

def address_detail(request, id):
    address = get_object_or_404(Address, id=id)
    return render(request, 'core/address_detail.html', {'address': address})

def address_create(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('address-list')
    else:
        form = AddressForm()
    return render(request, 'core/address_form.html', {'form': form})

def address_update(request, id):
    address = get_object_or_404(Address, id=id)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect('address-list')
    else:
        form = AddressForm(instance=address)
    return render(request, 'core/address_form.html', {'form': form})

def address_delete(request, id):
    address = get_object_or_404(Address, id=id)
    if request.method == 'POST':
        address.delete()
        return redirect('address-list')
    return render(request, 'core/address_confirm_delete.html', {'address': address})

# Order Views
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'core/order_list.html', {'orders': orders})

def order_detail(request, id):
    order = get_object_or_404(Order, id=id)
    return render(request, 'core/order_detail.html', {'order': order})

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order-list')
    else:
        form = OrderForm()
    return render(request, 'core/order_form.html', {'form': form})

def order_update(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order-list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'core/order_form.html', {'form': form})

def order_delete(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == 'POST':
        order.delete()
        return redirect('order-list')
    return render(request, 'core/order_confirm_delete.html', {'order': order})


# Geopy and nominatim

def all_addresses_map(request):
    state = request.GET.get('state')
    city = request.GET.get('city')
    neighborhood = request.GET.get('neighborhood')

    addresses = Address.objects.all()
    states = Address.objects.values_list('state', flat=True).distinct()
    cities = Address.objects.values_list('city', 'state').distinct()
    neighborhoods = Address.objects.values_list('neighborhood', 'state', 'city').distinct()

    if state:
        addresses = addresses.filter(state=state)
        cities = Address.objects.filter(state=state).values_list('city', 'state').distinct()
    if city:
        addresses = addresses.filter(city=city)
        neighborhoods = Address.objects.filter(state=state, city=city).values_list('neighborhood', 'state', 'city').distinct()
    if neighborhood:
        addresses = addresses.filter(neighborhood=neighborhood)

    # Calculate the center of the map based on filtered addresses
    center_lat, center_lon = -14.2350, -51.9253  # Default center: Brazil
    if addresses.exists():
        latitudes = [addr.latitude for addr in addresses if addr.latitude is not None]
        longitudes = [addr.longitude for addr in addresses if addr.longitude is not None]
        
        if latitudes and longitudes:
            center_lat = sum(latitudes) / len(latitudes)
            center_lon = sum(longitudes) / len(longitudes)
        else:
            # If no latitude/longitude, use geolocation based on other address fields
            geolocator = Nominatim(user_agent="core")
            location_str = state or city or neighborhood or None
            if location_str:
                location = geolocator.geocode(location_str)
                if location:
                    center_lat = location.latitude
                    center_lon = location.longitude

    m = folium.Map(location=[center_lat, center_lon], zoom_start=12)

    for address in addresses:
        lat, lon = address.latitude, address.longitude

        if lat is None or lon is None:
            location_str = None
            if address.zip_code:
                location_str = address.zip_code
            elif address.street:
                location_str = address.street
            elif address.neighborhood:
                location_str = address.neighborhood
            elif address.city:
                location_str = address.city
            elif address.state:
                location_str = address.state
            
            if location_str:
                location = geolocator.geocode(location_str)
                if location:
                    lat, lon = location.latitude, location.longitude

        if lat is not None and lon is not None:
            folium.Marker(
                [lat, lon],
                popup=f"{address.street}, {address.city}",
                tooltip=address.neighborhood
            ).add_to(m)

    map_html = m._repr_html_()

    return render(request, 'core/all_addresses_map.html', {
        'map_html': map_html,
        'state': state,
        'city': city,
        'neighborhood': neighborhood,
        'states': states,
        'cities': json.dumps(list(cities)),
        'neighborhoods': json.dumps(list(neighborhoods)),
    })


