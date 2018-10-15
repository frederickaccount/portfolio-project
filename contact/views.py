from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.views.generic import View
from django.http import HttpResponse # Add this

from .forms import ContactForm # Add this
from .models import Contact


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if request.POST['name'] and request.POST['email'] and request.POST['message']:
            # send email code goes here
            contact = Contact()
            contact.name = request.POST['name']
            contact.email = request.POST['email']
            contact.message = request.POST['message']
            contact.save()
            toSend = (contact.name + "\n" + contact.message )
            # return HttpResponse('Thanks for contacting me!')
            send_mail('Hello from frederickchute',
            toSend,
            contact.email,
            ['frederickchute@gmail.com'],
            fail_silently=False)
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
