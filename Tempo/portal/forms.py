from django import forms
from .models import Staff,Visitor
from datetime import datetime
STAFF_LIST=[[i.pk,i.staff_name] for i in Staff.objects.all()]
VISIT_TYPE=(('', 'Select Visit Type'),('Personal','Personal'),
('Official/Business','Official/Business'))

class VisitorsForm(forms.Form):
    visitorsname=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Visitor Name'}), label="")
    staff = forms.ChoiceField( choices=STAFF_LIST,required=True,widget=forms.Select(attrs={'class': 'btn btn-success dropdown-toggle'}),label="")
    visit_type=forms.ChoiceField(choices=VISIT_TYPE,required=True,widget=forms.Select(attrs={'class': 'btn btn-primary dropdown-toggle'}),label="")
    comment=forms.CharField(max_length=500,widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Additional Comment'}), label="")
    time_in=datetime.now()


#class Approval(forms.Form):
    # class VisitorForm(forms.Form):
    #     visitor_name = forms.CharField(
    #         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Visitor Name'}), label="")
    #     # staff_name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Staff Name'}),label="")
    #     staff_to_see = forms.ChoiceField(choices=STAFF_LIST,
    #                                      widget=forms.Select(attrs={'class': 'btn btn-success dropdown-toggle'}),
    #                                      label="", required=True)
    #     visit_type = forms.ChoiceField(choices=FORM_CHOICES,
    #                                    widget=forms.Select(attrs={'class': 'btn btn-primary dropdown-toggle'}),
    #                                    label="")
    #     # staff_mail = forms.EmailField(label="")
    #     comment = forms.CharField(
    #         widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Additional Comment'}), label="")


