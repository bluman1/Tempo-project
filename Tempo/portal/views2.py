from django.shortcuts import render, get_object_or_404
from .models import Staff,Visitor,VisitRequest
from sendgrid.helpers.mail import Email,Content,Mail
import sendgrid
from django.utils.translation import ugettext as _
from django.contrib import messages
from django.http import HttpResponseRedirect
sg = sendgrid.SendGridAPIClient('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')
from .forms import VisitorsForm
import secrets

 def token_generator():
    # code to generate random token here
    
 
 def send_request_mail(visit_request):
    # code to send mail to staff here
 
 
 def all_staff_view(request):
    # some sorta admin view for creating new staff
    if request.method == 'GET':
       staffs = Staff.objects.all()
       return render('stafs.html', {'staffs': staffs})
    elif request.method == 'POST':
       if request.POST.get('create_staff'):
          staff_name = request.POST.get('staff_name')
          staff_email = request.POST.get('staff_email')
          staff = Staff(staff_name=staff_name, staff_email=staff_email).save()
          staffs = Staff.objects.all()
          return render('staffs.html', {'staffs': staffs, 'created': 1})
 
def new_visit_requests(request):
   # this is the view for the guard people
   if request.method == 'GET':
       visit_requests = VisitRequest.objects.all().order_by('-timestamp')
       staffs = Staff.objects.all()
       return render('new_visit_requests.html', {'visit_requests': visist_requests, 'staffs': staffs})
    elif request.method == 'POST':
       if request.POST.get('create_request'):
          staff_id = int(request.POST.get('staff_id'))
          staff = Staff.objects.get(id=staff_id)
          visitor_name = request.POST.get('visitor_name')
          visitor = Visitor(visitor_name=visitor_name).save()
          reason = request.POST.get('reason')
          visit_request = VisitRequest(staff=staff, visitor=visitor, reason=reason, token=token_generator(), status=None).save()
          send_request_mail(visit_request=visit_request)
          # render view showing request created
          visit_requests = VisitRequest.objects.all().order_by('-timestamp')
          staffs = Staff.objects.all()
          return render('new_visit_requests.html', {'visit_requests': visist_requests, 'staffs': staffs, 'created': 1})


def show_visit_request(request, token):
   # this view is what staff sees when they click on the link in mail
   if request.method == 'GET':
      try:
         visit_request = VisitRequest.objects.get(token=token)
         return render('show_visit_request.html', {'visit_request': visit_request})
      except VisitRequest.DoesNotExist:
         return render('show_visit_request.html', {'does_notExist': 1})
   elif request.method == 'POST':
      if request.POST.get('approve'):
         visit_request = VisitRequest.objects.get(token=token)
         visit_request.status = True
         # if approved, how will guard at entrance know once it has been actioned? email sent to guard?
         visit_request.save()
         return render('show_visit_request.html', {'visit_request': visit_request})
      elif request.POST.get('disapprove')
         visit_request = VisitRequest.objects.get(token=token)
         visit_request.status = False
         # if disapproved, how will guard at entrance know once it has been actioned? email sent to guard?
         visit_request.save()
         return render('show_visit_request.html', {'visit_request': visit_request})
