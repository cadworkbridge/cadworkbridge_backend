from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from .models import HomeCard
from django.core.paginator import Paginator


def core(request):
    card_list = HomeCard.objects.all()
    paginator = Paginator(card_list, 6)  # 6 cards per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "core/core.html", {"page_obj": page_obj})


def contact(request):
    return render(request, "core/contact.html")