from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    #return HttpResponse("this is home page")
    return render(request,'home.htm')

def projects(request):
    return render(request,'projects.htm')
    
def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Profile details sumbitted!!!!!!!')

    return render(request,'contact.htm')