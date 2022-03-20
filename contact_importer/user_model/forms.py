from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()



# Sign Up Form
class SignUpForm(UserCreationForm):
    email = forms.EmailField(help_text="",label="", required=True, widget=forms.EmailInput(attrs={"class":"form-control", "placeholder":"Enter Email"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # For formatting the fields that are built in UserCreationForm
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs["class"] = "form-control"
        self.fields['username'].widget.attrs["placeholder"] = "Username"
        self.fields['username'].label = ""
        self.fields['username'].help_text = ""
        self.fields['password1'].widget.attrs["class"] = "form-control"
        self.fields['password1'].widget.attrs["placeholder"] = "Password"
        self.fields['password1'].label = ""
        self.fields['password2'].widget.attrs["placeholder"] = "Confirm Password"
        self.fields['password2'].widget.attrs["class"] = "form-control"
        self.fields['password2'].label = ""
        self.fields['password2'].help_text = ""