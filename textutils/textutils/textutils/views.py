from django.http import HttpResponse
from django.shortcuts import render
import string
def index(request):
    return render(request, 'index.html')

def analyze(request):
    #get the text
    djtext=request.POST.get('text','default')
    #check checkbox values
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps', 'off')
    newlineremover=request.POST.get('newlineremover', 'off')
    
    #check which checkbox is on
    if removepunc=='on':
        punctuations=string.punctuation
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        djtext=analyzed
    
    if (fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Changed To Uppercase', 'analyzed_text':analyzed}
        djtext=analyzed    
        
    if(newlineremover=='on'):
        analyzed=""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed=analyzed+char
        params={'purpose':'New Line Removed', 'analyzed_text':analyzed}
        djtext=analyzed   
    
    if not(removepunc=='on' and fullcaps=='on' and newlineremover=='on'):
        return render(request,'error.html')
    
    return render(request, 'analyze.html', params)    

