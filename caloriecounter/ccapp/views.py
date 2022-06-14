from django.shortcuts import render
from ccapp.forms import RegistrationForm

from ccapp.forms import LoginForm

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

        context = {
            'form': login_form,
            'data': {
                    'email': email,
                    'password': password
                }
            }
        return render(request, template, context)
    else:
        context = {'form': login_form}
        return render(request, template, context)
        

def user_register(request):
    register_form = RegistrationForm()
    template = 'users/create.html'
    context = {'form': register_form}
    return render(request, template, context)


def user_index(request):
    # render() - use to render the templates/pages
    # this function takes three parameter
    # 1. request - request from the client
    # 2. template - html page direction
    # 3. context - data that are passed to templates ( must be of type dict ) - is optional
    template = 'users/index.html'
    context = {
        'page_content_title': 'User Dashboard',
        'page_content_body': 'Welcome to calorie counter.'
    }

    return render(request, template, context)