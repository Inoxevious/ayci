from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import AccountUser
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, DelegationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your AYCi Account'
           
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account:account_activation_sent')

    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def account_activation_sent(request):

    return render(request, 'registration/account_activation_sent.html')

def activate(request, uidb64, token):
    form = DelegationForm(request.POST)
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if request.method == 'POST':
        
        if form.is_valid():
            if user is not None and account_activation_token.check_token(user, token):
                user.is_active = True
                user.accountuser.email_confirmed = True
                user.accountuser.country = form.cleaned_data.get('country')
                user.accountuser.role = form.cleaned_data.get('role')
                user.save()
                login(request, user)
                return render(request,'home.html')
            else:
                return render(request, 'registration/account_activation_invalid.html')

    else:
        form = DelegationForm()
    return render(request, 'registration/delegation.html', {'form': form})




@login_required(login_url='/accounts/login/')
def index(request, **kwargs):
        farmer = "farmer"
        investor ="investor"
        invest_manager = "invest manager"
        agent = "agent"
        processor = "processor"
        user_url = ''

        user_id = request.user.id
        account_user = AccountUser.objects.get(user_id=user_id)
 

        if str(account_user.user_class) == farmer:
            user_url = 'farmer' 

        elif str(account_user.user_class) == investor:
            user_url = 'investor'
                   
        elif str(account_user.user_class) == invest_manager:
            user_url = 'investmanager'
          
        elif str(account_user.user_class) == agent:
            user_url = 'agent'
        
        elif str(account_user.user_class) == processor:
            user_url = 'processor'
    
        else:
            user_url = 'registration/login.html'
        
        return HttpResponseRedirect(reverse(user_url, kwargs={'user_id': user_id }))


def home(request):

    name = request.user.accountuser.role



    return render(request, 'home.html', {'name':name})
