from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import CustomSignUpForm

class SignUp(CreateView):
    model = User
    form_class = CustomSignUpForm
    success_url = '/accounts/login/'
    template_name = 'registration/signup.html'


# Create your views here.
