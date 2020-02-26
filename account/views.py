from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from .models import AccountUser
from articles.models import Author
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, DelegationForm
from django.contrib.auth import  authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib import messages, auth
from  . choices import price_choices, bedroom_choices, state_choices, countries_choices, role_choices, writer_choices
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
# 
def dashboard(request):
    user_contacts = Contact.objects.filter(user_id = request.user.id).order_by('-contact_date')

    context = {
        'contacts': user_contacts,
    }
    return render(request,'accounts/dashboard.html',context)


def login(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       user = auth.authenticate(username = username,password = password)

       if user:
          auth.login(request,user)
          acc = AccountUser.objects.get(user_id = user.id)
          if acc.writer == True:
              return redirect('admin/')
          else:

              messages.success(request,"You are now logged in.")
              return redirect('index')
       else:
            messages.error(request,"Invalid Credentials")
            return redirect('login')       
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,"Logged Out")
    return redirect('index')

def register(request):
    
    if request.method == "POST":
        dcountry = 'africa'
        drole = 'member'
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        try:
            country = request.POST['country']
        except MultiValueDictKeyError:
            country = 'africa'
            
        try:
            role = request.POST['role']
        except MultiValueDictKeyError:
            role = 'member'

        try:
            postwriter = request.POST['writer']
        except MultiValueDictKeyError:
            postwriter = False


        
        
        
        
        writer = False
        updated_writer = writer

        if postwriter == 'yes':
            writer = True
        else:
            writer = False
        
        updated_writer = writer


        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username = username).exists():
                messages.error(request,"That username is taken.")
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.error(request,"That email is taken.")
                    return redirect('register')
                else:
                    # looks good
                    
                    user = User.objects.create_user(username = username,
                    password = password,email=email,first_name = first_name,
                    last_name = last_name )
                    user.save()



                    user = get_object_or_404(User, email = email)              
                    acc = get_object_or_404(AccountUser, user_id = user.id)
                    acc.role = role
                    acc.country = country
                    acc.email = email
                    acc.writer = updated_writer
                    acc.save()

                    if updated_writer == True:
                        user.is_staff = True 
                        user.save()  

                    # Login after register
                    auth.login(request,user)
                    messages.success(request,"You are now logged in.")
                    return redirect('login')

                    # # Login manually 
                    # messages.success(request,"You can now log in.")
                    # return redirect('login')
        else:
            messages.error(request,'Passwords do not match.')
            return redirect('register')
    else:
        context = {
            'countries_choices' :countries_choices,
            'role_choices': role_choices,
            'writer_choices' : writer_choices,
        }
        return render(request,'accounts/register.html' , context)




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




# @login_required(login_url='/accounts/login/')
# def index(request, **kwargs):
#         farmer = "farmer"
#         investor ="investor"
#         invest_manager = "invest manager"
#         agent = "agent"
#         processor = "processor"
#         user_url = ''

#         user_id = request.user.id
#         account_user = AccountUser.objects.get(user_id=user_id)
 

#         if str(account_user.user_class) == farmer:
#             user_url = 'farmer' 

#         elif str(account_user.user_class) == investor:
#             user_url = 'investor'
                   
#         elif str(account_user.user_class) == invest_manager:
#             user_url = 'investmanager'
          
#         elif str(account_user.user_class) == agent:
#             user_url = 'agent'
        
#         elif str(account_user.user_class) == processor:
#             user_url = 'processor'
    
#         else:
#             user_url = 'registration/login.html'
        
#         return HttpResponseRedirect(reverse(user_url, kwargs={'user_id': user_id }))


def home(request):

    name = request.user.accountuser.role



    return render(request, 'home.html', {'name':name})

def index(request):

    return render(request, 'index.html')