from django.urls import path
from . import views
from .views import create_customer

urlpatterns = [
    path('customer/create/', create_customer, name='create_customer'),
    path('', views.index, name='index'),
    path('customers/', views.customer_list, name='customer-list'),
    path('customers/<int:id>/', views.customer_detail, name='customer-detail'),
    path('customers/<int:id>/details', views.customer_detail_with_details, name='customer-details'),
    path('customers/create/', views.customer_create, name='customer-create'),
    path('customers/<int:id>/update/', views.customer_update, name='customer-update'),
    path('customers/<int:id>/delete/', views.customer_delete, name='customer-delete'),
    path('customers/map/<int:id>/', views.customer_detail_with_map, name='customer-detail-with-map'),
    
    path('addresses/', views.address_list, name='address-list'),
    path('addresses/<int:id>/', views.address_detail, name='address-detail'),
    path('addresses/create/', views.address_create, name='address-create'),
    path('addresses/<int:id>/update/', views.address_update, name='address-update'),
    path('addresses/<int:id>/delete/', views.address_delete, name='address-delete'),
    path('addresses/map/', views.all_addresses_map, name='all-addresses-map'),
    
    path('orders/', views.order_list, name='order-list'),
    path('orders/<int:id>/', views.order_detail, name='order-detail'),
    path('orders/create/', views.order_create, name='order-create'),
    path('orders/<int:id>/update/', views.order_update, name='order-update'),
    path('orders/<int:id>/delete/', views.order_delete, name='order-delete'),
]
