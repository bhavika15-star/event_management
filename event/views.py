from django.shortcuts import render,HttpResponse
from event.models import Contact,Payment

# Create your views here.
def event(request): 
    return render(request, 'home.html')

def about(request): 
    return render(request, 'about.html')


def payment(request):
    if request.method=="POST":
        firstname=request.POST.get('firstName')
        lastname=request.POST.get('lastName')
        username=request.POST.get('username')
        email=request.POST.get('email')
        address=request.POST.get('address')
        zip=request.POST.get('zip')
        payment=request.POST.get('payment')
        cardname=request.POST.get('cc-name')
        cardno=request.POST.get('cc-number')
        expiration=request.POST.get('cc-expiration')
        cvv=request.POST.get('cc-cvv')
        payment=Payment(firstname=firstname,lastname=lastname,username=username,email=email,address=address,zip=zip,payment=payment,cardname=cardname,cardno=cardno,expiration=expiration,cvv=cvv)
        payment.save()
        return render(request,'thanks.html')
    return render(request, 'payment.html')
 

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        Phone=request.POST.get('Phone')
        message=request.POST.get('message')
        contact=Contact(name=name,email=email,Phone=Phone,message=message)
        contact.save()
        return render(request,'thanks.html')
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def bday(request):
    return render(request,'bday.html')

def wedding(request):
    return render(request, 'wedding.html')

def concert(request):
    return render(request, 'concert.html')

def thanks(request):
    return render(request, 'thanks.html')
