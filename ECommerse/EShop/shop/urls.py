from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about', views.about, name="AboutUs"), 
    path('contact', views.contact, name="ContactUs"), 
    path('contact/success', views.contact_success, name="contact_success"),
    path('tracker', views.tracker, name="TrackingStatus"), 
    path('search', views.search, name="Search"), 
    path("products<int:myid>", views.productView, name="ProductView"), 
    path('checkout', views.checkout, name="checkout"),
    path("products", views.productView, name="productView"),  
    
    
    
]