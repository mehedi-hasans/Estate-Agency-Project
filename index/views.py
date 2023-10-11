from contact.models import Message
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):


    # send_mail(
    #     "Subject here",
    #     "Here is the message.",
    #     "mehedi@gmail.com",
    #     ["mehedi4969@gmail.com"],
    #     fail_silently=False,
    # )


    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def agent(request):
    return render(request, 'agent-single.html')

def dashboard(request):

    item =Message.objects.all()

    return render(request, 'dashboard.html', {'item': item})

def agents(request):





    return render(request, 'agents-grid.html')

def blog(request):
    return render(request, 'blog-grid.html')

def blogSingle(request):
    return render(request, 'blog-single.html')

def property(request):
    return render(request, 'property-grid.html')

def propertySingle(request):
    return render(request, 'property-single.html')


