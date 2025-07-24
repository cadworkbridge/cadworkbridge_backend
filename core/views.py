from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages

def core(request):
    # return redirect('swagger-ui')
    return render(request, 'core/core.html')
