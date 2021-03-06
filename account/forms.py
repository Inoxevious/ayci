from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import AccountUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    date_birth = forms.DateField(help_text='Required. Format: YYYY-NN-DD')
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'date_birth', 'email', 'password1', 'password2', )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-signUpForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'SignUp'))

class DelegationForm(forms.Form):
    country = forms.CharField(max_length=30, required=False, help_text='Optional.')
    role = forms.CharField(max_length=30, required=False, help_text='Optional.')
    

    class Mate:
        model = AccountUser
        fields = ('country', 'role',)
    
    def __init__(self, *args, **kwargs):
        super(DelegationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-delegationForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Continue'))