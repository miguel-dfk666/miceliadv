from django.db import models
from .forms import UserRegister
from django.views.generic import FormView

# Create your models here.

# UserRegister is a simple class that allows you to register a user using Django
class Registrar(FormView):
  template = 'register.html'
  form_class = UserRegister