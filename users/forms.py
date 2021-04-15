from django.contrib.auth.models import User
from django import forms
from allauth.account.forms import SignupForm

class LoginForm(forms.ModelForm):
    '''Simple login form'''
    class Meta:
        model = User
        fields = ('username', 'password')


class MyCustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['usertype'] = forms.ChoiceField(choices=[(1, "Candidate"),
                                                             (0, "Recruiter")],
                                                    widget=forms.RadioSelect)

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.usertype = self.cleaned_data.pop('usertype')
        user.save()
        return user
        
        