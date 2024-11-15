from django.shortcuts import render, HttpResponse

# Create your views here.
def blogHome(request):
    return HttpResponse('This is home')

def blogPost(request, slug): 
    return HttpResponse(f'This is blogPost : {slug}')
