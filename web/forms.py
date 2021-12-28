from django import forms
from django.forms import ModelForm, widgets
from web.models import Contact
from django.forms.widgets import EmailInput, TextInput, Select
from django import forms 
from web.models import COMPANY_SIZE, INDUSTRY, JOB_ROLE, COUNTRY



EMPTY_COMPANY_SIZE = (("","Company Size"),) + COMPANY_SIZE
EMPTY_INDUSTRY = (("","Industry"),) + INDUSTRY
EMPTY_JOB_ROLE = (("","Job Rule"),) + JOB_ROLE
EMPTY_COUNTRY = (("","Country"),) + COUNTRY

class ContactForm(ModelForm):
    company_size = forms.ChoiceField(choices=EMPTY_COMPANY_SIZE)
    industry = forms.ChoiceField(choices=EMPTY_INDUSTRY)
    job_role = forms.ChoiceField(choices=EMPTY_JOB_ROLE)
    country = forms.ChoiceField(choices=EMPTY_COUNTRY)


    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "email": widgets.EmailInput(attrs={"placeholder":"Enter Your Email"}),
            "first_name": widgets.TextInput(attrs={"placeholder":" First Name"}),
            "last_name": widgets.TextInput(attrs={"placeholder":" Last Name"}),
            "company": widgets.TextInput(attrs={"placeholder":"Company Name"}),
            "company_size": widgets.Select(attrs={"placeholder":"Enter Your Email"})
        }