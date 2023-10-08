from django.shortcuts import render
from .models import Message
# Create your views here.
def contact(request):
    messagedata =Message.objects.all()
    context = {
        'message' : messagedata,
    }

    return render(request, 'contact.html', context)

