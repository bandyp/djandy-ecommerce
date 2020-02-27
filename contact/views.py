from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from accounts.models import Profile
from accounts.forms import UserLoginForm, UserRegistrationForm, ProfileUpdateForm, UserUpdateForm



@login_required
def contact(request):
    # calls up form and sends email, sends a message to template to confirm message sent
    instance = request.user
    if request.method == 'POST':
        form = ContactForm(request.POST, initial=instance)
        if form.is_valid():
            
            sender_name = form.cleaned_data['username']
            sender_email = form.cleaned_data['email']

            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, ['enquiry@exampleco.com'])
            messages.success(request, "Thankyou for your request. We will be in touch shortly.")
            return render(request, 'message.html', {'form': form})
    form = ContactForm(initial={'username': instance.get_username(), 'email': instance.email}, auto_id=False)
    print(form)       
    return render(request, 'contact.html', {'form': form})

