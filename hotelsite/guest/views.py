from django.shortcuts import render

def guest_home(request):
    return render(request, 'guest/guest_home.html')

def payment(request):
    return render(request, 'guest/payment.html')
# Create your views here.
