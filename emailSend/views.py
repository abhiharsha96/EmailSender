from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
from django.conf import settings
def greetings(request):
        return render(request,'index.html')
def contact(request):
       if request.method == "POST":
                Subject_mail = request.POST['Subject']
                Message_mail = request.POST['Message']
                Email_mail_To = request.POST['To']
                settings.EMAIL_HOST_USER= request.POST['From']
                settings.EMAIL_HOST_PASSWORD=request.POST['Password']

                send_mail(
                Subject_mail,
                Message_mail,
                settings.EMAIL_HOST_USER,
                [Email_mail_To,'abhiharsha54@gmail.com'],
                fail_silently=False
                )  
                return render(request,'index.html',{'Message_mail':Message_mail})
       else:   
                return render(request,'index.html')
                       

