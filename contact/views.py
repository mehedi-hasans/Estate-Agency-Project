from django.shortcuts import redirect, render
from .models import Message
# Create your views here.
def contact(request):
    item  = Message.objects.all()
    # context = {}
    if request.method=='POST':
        myName=request.POST.get("name")
        myEmail=request.POST.get("email")
        mySubject=request.POST.get("subject")
        myMessage=request.POST.get("message")
        item =Message.objects.all()
        messagedata = Message(
            name=myName,
            email=myEmail,
            subject=mySubject,
            message=myMessage,

        )
        messagedata.save()
        
        return render(request, 'contact.html', {'item': item})

    return render(request, 'contact.html', {'item': item})

