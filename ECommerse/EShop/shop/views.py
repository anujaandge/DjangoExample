from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Product, Contact

from math import ceil
# Create your views here.

def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
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
            recipient_list=['goreanuja6@gmail.com'],  # Replace with your admin email
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

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request, myid):
    product=Product.objects.filter(id=myid)
    print(f"Product {product}")
    return render(request, 'shop/prodView.html',{'product':product[0]})

def checkout(request):
    return render(request, 'shop/checkout.html')
