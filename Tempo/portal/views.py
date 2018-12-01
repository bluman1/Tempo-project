from django.shortcuts import render, get_object_or_404
from .models import Staff,Visitor,Requests
from sendgrid.helpers.mail import Email,Content,Mail
import sendgrid
from django.utils.translation import ugettext as _
from django.contrib import messages
from django.http import HttpResponseRedirect
sg = sendgrid.SendGridAPIClient('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')
from .forms import VisitorsForm
import secrets

def formpage(request):
    if request.method=='POST':
        token=secrets.token_urlsafe(20)
        visitor_name=request.POST.get('visitorsname')
        comment=request.POST.get('comment')
        visit_type=request.POST.get('visit_type')
        visit_content='You have a waiting visitor'+'\n'+'Name:'+visitor_name+'\n'+'Purpose Of Visit:'+visit_type+'\n'+'Additional Comment:'+comment+'\n'+token
        staff_id=request.POST.get('staff')
        staff=Staff.objects.get(id=staff_id)
        staff_email=staff.staff_email
        req_comment = request.POST.get('req_comment')
        request_id = (request.POST.get('request_id'))
        # requests = Requests.objects.get(id=request_id)
        # requests.comment = req_comment
        # requests.save()
        # req=Requests.objects.get(id=request_id)
        visitor=Visitor(staff=staff,visitor_name=visitor_name,token=token).save()
        request=Requests(staff=staff,visitor=Visitor.objects.get(id=staff_id)).save()


        from_email = Email("Tempo_security@tempong.com")
        to_email = Email(staff_email)
        subject = visitor_name
        content = Content("text/plain",visit_content)
        mail= Mail(from_email, subject, to_email, content)
        response=sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        print(response.headers)
        if response.status_code==200:
            messages.add_message(request,messages.SUCCESS,_('Mail sent'))
        elif response.status_code==202:
            messages.add_message(request,messages.SUCCESS,_('Mail sent for processing'))
        else:
            messages.add_message(request,messages.ERROR,_('Mail not sent'))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
        
    else:
        form=VisitorsForm()
        context = {'form':form}
        return render(request, 'portal/formpage.html', context)
        
def sendgrida(request):
    return render(request, 'portal/sendgrida.py')

def requests(request):
    visitors=Visitor.objects.all()
    # requests = Requests.objects.get()
    context={
        'visitors':visitors,
        'requests':requests
    }
    if request.POST.get('request_id'):
        request_id = int(request.POST.get('request_id'))
        visitor = Visitor(visit_status=request_id).save()

    return render(request,'portal/requests.html',context)

def approval(request,staff_id):
    staff=get_object_or_404(Staff, id=staff_id)
    visitors=Visitor.objects.all()

    requests = Requests.objects.all().order_by('status')
    context = {
        'staff': staff,
        'requests': requests,
        'visitors':visitors
    }
    return render(request, 'portal/approval.html',context)