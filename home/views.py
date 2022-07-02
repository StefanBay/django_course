from django.shortcuts import render
#own imports
from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.datetime.today()}

class AuthorizedView(LoginRequiredMixin, TemplateView): # not used anymore
    template_name = 'home/authorized.html'
    login_url = '/login'

class LoginInterfaceView(LoginView):
    """User Login interface of the application """
    template_name = 'home/login.html'

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

class SignupView(CreateView):
    """ Signup form for new users """
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'
    
    def get(self, request, *args, **kwargs):
        """Allows only logged out users to create a new user"""
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request,*args, **kwargs)


# def home(request):
#     return render(request, 'home/welcome.html',{'today': datetime.datetime.today()})

# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request,'home/authorized.html',{})
