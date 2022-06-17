from operator import ge
from django.shortcuts import render
from ccapp.models import AppUser
from ccapp.forms import RegistrationForm
from datetime import datetime
from ccapp.forms import LoginForm
import random
#  send email package
from django.core.mail import send_mail

# Create your views here.
def landing(request):
    template = 'index.html'
    context = {
        'page_content_title': 'Home Page',
        'msg_welcome': 'Welcome to calorie counter.'
    }
    return render(request, template, context)

def user_login(request):        
    login_form = LoginForm()
    template = 'users/login.html'
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        # checking and selecting user object from database with email
        user = AppUser.objects.get(email=email)
        if password == user.password:
            # storing user credentials in session
            # request.session.setdefault('user_email', user.email)
            request.session['user_email'] = user.email
            # request.session.update({'user_email': user.email})
            # checking session value and redirecting to index page
            if request.session.has_key('user_email'):
                template = "users/index.html"
                context = {
                    'form': login_form,
                    'data': {
                            'email': user.email,
                            'page_content_title': 'User Dashboard',
                            'page_content_body': 'Welcome to calorie counter:- '
                        }
                    }
                return render(request, template, context)
        else:
            context = {
                'form': login_form
                }
            return render(request, template, context)
    else:
        context = {'form': login_form}
        return render(request, template, context)
        
def user_register(request):
    register_form = RegistrationForm()
    template = 'users/create.html'

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        middle_name = request.POST['middle_name']
        last_name = request.POST.get('last_name')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        blood_group = request.POST.get('blood_group')
        password = request.POST.get('password')

        # creating user object 
        # method one non-parameterized constructor
        # user = AppUser()
        # user.first_name = first_name
        # user.middle_name = middle_name
        # user.last_name = last_name
        # user.contact = contact
        # user.email = email
        # user.gender = gender
        # user.dob = dob
        # user.blood_group = blood_group
        # user.created_at = datetime.now()
        # user.password = password
        vc = random.random()
        # method with parameterized constructor
        user = AppUser(first_name=first_name,\
            middle_name=middle_name,last_name=last_name,\
                contact=contact, email=email, gender=gender, \
                    dob=dob, blood_group=blood_group, password=password,\
                        created_at=datetime.now(),\
                            verification_code=vc)
        # to store data
        user.save()

        send_mail(
            'Calori Counter Email Verification',
            'Your email verification code is: ' + str(user.verification_code),
            'c4crypt@gmail.com',
            [user.email],
            fail_silently=False
        )
        context = {'form': register_form}
        return render(request, template, context)
    else:
        context = {'form': register_form}
        return render(request, template, context)

def user_logout(request):
    if request.session.has_key('user_email'):
        del request.session['user_email']
        login_form = LoginForm()
        template = "users/login.html"
        context = {
            'form': login_form
            }
        return render(request, template, context)

def user_index(request):
    # render() - use to render the templates/pages
    # this function takes three parameter
    # 1. request - request from the client
    # 2. template - html page direction
    # 3. context - data that are passed to templates ( must be of type dict ) - is optional
    if request.session.has_key('user_email'):
        template = 'users/index.html'
        context = {
            'page_content_title': 'User Dashboard',
            'page_content_body': 'Welcome to calorie counter.'
        }

        return render(request, template, context)
    else:
        login_form = LoginForm()
        template = "users/login.html"
        context = {
            'form': login_form
            }
        return render(request, template, context)