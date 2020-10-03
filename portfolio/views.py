from django.shortcuts import render, HttpResponseRedirect
from .models import Project
from .models import Contacts
from .contact_form import NewContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/index.html', {'projects': projects})

def about(request):
    return render(request, 'portfolio/about.html')

def services(request):
    return render(request, 'portfolio/services.html')

def contact(request):
    contact_detail = Contacts.objects.all();
    template = "contact.html"
    user_contact = None
    if request.method == 'POST':
        contact_form = NewContactForm(request.POST or None)
        if contact_form.is_valid():
            data = contact_form.cleaned_data
            get_subj = data['subject']
            get_name =  data['name']
            get_email = data['email']
            get_msg =  data['message']
        #    send_mail(get_subj, get_msg, get_email, ['fetex3252625@gmail.com'],fail_silently = False)
            contact_form.save()

            return HttpResponseRedirect('/contact')
            messages.success(request, 'Successfully Sent The Message!')

    else:
        contact_form = NewContactForm()
    context = {
        'contact_form': contact_form,
    }
    return render(request, 'portfolio/contact.html', context)
