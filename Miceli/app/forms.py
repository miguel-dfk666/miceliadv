from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# cirar conta
class UserRegister(UserCreationForm):
  email = forms.EmailField(required=True)
  
  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')
  def OnSave(self):
    user = super(UserRegister, self).OnSave(commit=False)
    user.email = self.cleaned_data['email']
    if commit:
      user.OnSave()
    return user
  