from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    '''Simple login form'''
    class Meta:
        model = User
        fields = ('username', 'password')