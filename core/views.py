from django.shortcuts import render

def core(request):
    return render(request, 'core/core.html')

def contact(request):
    return render(request, 'core/contact.html')