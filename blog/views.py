from django.shortcuts import render
from django.contrib import messages
from .models import blog , Contact
# Create your views here.

def home(request):
    blogs = blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})

def about(request):
    return render(request, 'about.html')

def login_page(request):
    return render(request, 'login.html')

def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        form = Contact(email=email, subject=subject, message=message)

        # Saving Form data to Database
        messages.success(request, 'Your message is Sent :) ')
        form.save()

        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')