from django.shortcuts import render
from .models import Works
from django.core.mail import  send_mail
from django.conf import settings
def index(request):
    works = Works.objects.all()
    context = {"works":works}
    if request.method == 'POST':
        print("post")
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')
        to_email = "allamco4@gmail.com"
        email_from = settings.EMAIL_HOST_USER
        msg = "allam you receive a message from Mr {} , where is email is  {} , which he say :  {}".format(name, email,  message)
        send_mail(subject, msg, email_from, [to_email])
    return render(request,'index.html',context)
