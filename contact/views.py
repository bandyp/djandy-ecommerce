from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from accounts.models import Profile
from accounts.forms import UserLoginForm, UserRegistrationForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.models import User

def contact(request):
    # calls up form and sends email, sends a message to template to confirm message sent
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=request.user)
        if form.is_valid():
            
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, ['enquiry@exampleco.com'])
            messages.success(request, "Thankyou for your request. We will be in touch shortly.")
            return render(request, 'message.html', {'form': form})
    form = ContactForm(initial={'name': 'instance', 'email':'instance'}, auto_id=False)
    print(form)       
    return render(request, 'contact.html', {'form': form})
"""    
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
        messages.success(request, f"Your account has been updated")
        return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    return render(request, 'profile.html', {'p_form': p_form, 'u_form': u_form})
"""