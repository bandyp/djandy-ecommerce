from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponse('Thanks for contacting us, we will reply shortly')
    else:
        form = ContactForm()
        
    return render(request, 'contact.html', {'form': form})