from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(
        max_length=18,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Username",
                "required": True,
                "max-length": 18,
            }
        ),
    )
    name = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Name",
                "required": True,
                "max-length": 12,
            }
        ),
    )
    surname = forms.CharField(
        max_length=14,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Last Name",
                "required": True,
                "max-length": 14,
            }
        ),
    )
    email = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-input", "placeholder": "Email", "required": True}
        ),
    )
    password = forms.CharField(
        max_length=190,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Password",
                "required": True,
                "type": "password",
            }
        ),
    )
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields["username"].label = False
        self.fields["name"].label = False
        self.fields["surname"].label = False
        self.fields["email"].label = False
        self.fields["password"].label = False

class SignInForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-input", "placeholder": "Username", "required": True}
        ),
    )
    password = forms.CharField(
        max_length=190,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Password",
                "required": True,
                "type": "password",
            }
        ),
    )
    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.fields["username"].label = False
        self.fields["password"].label = False

class UpdateProfileForm(forms.Form):
    username = forms.CharField(
        max_length=18,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Username",
                "required": True,
                "max-length": 18,
            }
        ),
    )
    name = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Name",
                "required": True,
                "max-length": 12,
            }
        ),
    )
    surname = forms.CharField(
        max_length=14,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Last Name",
                "required": True,
                "max-length": 14,
            }
        ),
    )
    password = forms.CharField(
        max_length=190,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Password",
                "required": True,
                "type": "password",
            }
        ),
    )
    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        self.fields["username"].label = False
        self.fields["name"].label = False
        self.fields["surname"].label = False
        self.fields["password"].label = False