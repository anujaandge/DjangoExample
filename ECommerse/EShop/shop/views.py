from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Product, Contact, Order, OrderUpdate

from math import ceil
import json
# Create your views here.

def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        
        # Email to Admin
        admin_message = f"New contact request:\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:\n{desc}"
        send_mail(
            subject="New Contact Request - Mayinsoft.com",
            message=admin_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['your admin email'],  # Replace with your admin email
        )
        #confirmation Email to User
        user_message = f"Hello {name},\n\nThank you for contacting Mayinsoft.com. We have received your message:\n\n{desc}\n\nWe will get back to you shortly.\n\nBest,\nMayinsoft.com Team"
        send_mail(
            subject="Thank you for reaching out to Mayinsoft.com",
            message=user_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
        )
        # Redirect to a thank-you page or display success message
        return redirect('contact_success')  
    return render(request, 'shop/contact.html')

def contact_success(request):
    return render(request, 'shop/contact_success.html')

from django.http import JsonResponse

def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if order.exists():
                updates = OrderUpdate.objects.filter(order_id=orderId)
                update_list = [{'text': item.update_desc, 'time': item.timestamp} for item in updates]
                return JsonResponse(update_list, safe=False)  # Returns JSON response directly
            else:
                return JsonResponse([], safe=False)  # Returns empty list if no order found
        except Exception as e:
            print(f"Error in tracker view: {e}")
            return JsonResponse([], safe=False)  # Returns empty list in case of an error

    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')

def productView(request, myid):
    product=Product.objects.filter(id=myid)
    print(f"Product {product}")
    return render(request, 'shop/prodView.html',{'product':product[0]})

def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        address=request.POST.get('address1','') + request.POST.get(' address2','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip_code=request.POST.get('zip_code','')
        phone=request.POST.get('phone','')
        
        order=Order(items_json=items_json,name=name, email=email, phone=phone, address=address,city=city, state=state,zip_code=zip_code)
        order.save()
        update= OrderUpdate(order_id= order.order_id, update_desc="The order has been placed")
        update.save()
        thank=True
        id=order.order_id
        print(id)
        # return redirect('checkout_success',{'id':id})  
        return render(request, 'shop/checkout.html', {'thank':thank, 'id':id})
    return render(request, 'shop/checkout.html')

def checkout_success(request):
    return render(request, 'shop/checkout_success.html')
