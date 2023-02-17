from django.shortcuts import render, redirect
from django.core.mail import EmailMessage, send_mail
from .forms import Formulario


# Create your views here.
def contact(request):
    formulario=Formulario()
    if request.method=='POST':
        formulario=Formulario(data=request.POST)
        if formulario.is_valid():
            name= request.POST.get('name')
            email= request.POST.get('email')
            subject= request.POST.get('subject')
            message= request.POST.get('message')

            #Send email
        
            email_s=EmailMessage('from the web',
                f'{name} with {email} and subject: {subject} send this message:\n\n {message}',
                'EMAIL_HOST_USER',
                ['fran.martinez.clavijo@gmail.com'],
                )
            
            fail_silently=False
            email_s.send()
            try: 
                return redirect('/contact/?ok')
            except:
                return redirect('/contact/?noOk')



    return render(request,'contacto/contact.html', {'form':formulario})