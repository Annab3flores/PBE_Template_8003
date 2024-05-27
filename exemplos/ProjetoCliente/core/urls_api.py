from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.CustomerList.as_view(), name='customer-list'),
    path('customers/<int:pk>/', views.CustomerDetail.as_view(), name='customer-detail'),
    path('addresses/', views.AddressList.as_view(), name='address-list'),
    path('addresses/<int:pk>/', views.AddressDetail.as_view(), name='address-detail'),
    path('orders/', views.OrderList.as_view(), name='order-list'),
    path('orders/<int:pk>/', views.OrderDetail.as_view(), name='order-detail'),
]