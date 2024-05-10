from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,'frontend/index.html')

def aboutpage(request):
    return render(request,'frontend/about.html')

def servicepage(request):
    return render(request,'frontend/services.html')

def reservationpage(request):
    return render(request,'frontend/reservation.html')

def contactpage(request):
    return render(request,'frontend/contact.html')

def testimonialspage(request):
    return render(request,'frontend/testimonials.html')

def menupage(request):
    return render(request,'frontend/menu.html')

