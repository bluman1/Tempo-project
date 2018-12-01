# import sendgrid
# import os
# from sendgrid.helpers.mail import *
#
# visitor_name = formData.getvalue('visitor_name')
# sg = sendgrid.SendGridAPIClient('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')
# from_email = Email("Tempo_security@example.com")
# to_email = Email(staff_name)
# subject = ""
# content = Content("")
# mail = Mail(from_email, subject, to_email, content)
# response = sg.client.mail.send.post(request_body=mail.get())
# print(response.status_code)
# print(response.body)
# print(response.headers)

import sendgrid
import os
import cgi
from sendgrid.helpers.mail import *

#you don't need this file anymore
def getData():
  formData = cgi.FieldStorage()
  staff_name = formData.getvalue('staff_name')
  visitor_name= formData.getvalue('visitor_name')
  staff_email= staff_name.replace(" ", "") + '@yahoo.com'
  return staff_email, visitor_name

def sender():
  sg = sendgrid.SendGridAPIClient('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')
  from_email = Email("Tempo_security@example.com")
  to_email = Email()
  subject = "Sending with SendGrid is Fun"
  content = Content("text/plain", "and easy to do anywhere, even with Python")
  mail = Mail(from_email, subject, to_email, content)
  response = sg.client.mail.send.post(request_body=mail.get())
  print(response.status_code)
  print(response.body)
  print(response.headers)



