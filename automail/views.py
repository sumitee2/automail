from django.http import HttpResponse


from django.core.mail import send_mail



def send_email(request):
    mail_title = 'Hello!'
    message = 'Have you received this mail?'
    email = 'shifuwhite@gmail.com'
    recipients = ['sumit@ophio.co.in',]
    resp = send_mail(mail_title, message, email, recipients)


    html = "<html><body>It is now. " + resp.__str__() + " </body></html>" 
    return HttpResponse(html)