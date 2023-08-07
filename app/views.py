from django.shortcuts import render
from .models import Main,Flat
import smtplib, ssl
# Create your views here.

def index(request):
    number = request.POST.get('num')
    a = request.POST.get('nm')
    print(a)
    print(number)
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "rafatkamel96@gmail.com"  # Enter your address
    receiver_email = "pemot94942@muzitp.com"  # Enter receiver address
    password = 'dtkbakxiemjbjizz'
    message = message = f"""\
    Subject: Hi there

    Someone asks for the apartment code ({a})
    his number is ({number})."""
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    context ={
        'main' : Main.objects.all(),
        'about': Main.objects.get(iid = 1)
    }    
    return render(request,'index.html',context)




def flat(request):
    a = request.POST.get('hid_id')
    print(a)
    context ={
        'main' : Flat.objects.get(iid = a),
        'b' : Main.objects.get(iid = a),
    }

    return render(request,'flat.html',context)







