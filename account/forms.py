from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm

from account.models import User

class EmployeeRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        UserCreationForm.__init__(self, *args, **kwargs)
        self.fields['gender'].required = True
        self.fields['username'].label = "Username"
        self.fields['email'].label = "Email"
        self.fields['phoneNumber'].label = "Phone Number"
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"
        self.fields['gender'].label = "Gender"

        self.fields['username'].widget.attrs.update(
            {
                'placeholder': 'Enter Username',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['phoneNumber'].widget.attrs['class'] = 'number'
        self.fields['phoneNumber'].widget.attrs.update(
            {
                'placeholder': 'Enter Phone Number',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )
        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Last Name',
            }
        )
        self.fields['category'].widget.attrs.update(
            {
                'placeholder': 'Enter Last Name',
            }
        )
        skills = forms.Textarea()
        qualifications = forms.Textarea()
        experiences = forms.Textarea()
        resume = forms.FileField()

    class Meta:

        model = User

        fields = ['username', 'email', 'password1', 'password2', 'phoneNumber', "category",
				'first_name', 'last_name', 'gender', 'skills', 'qualifications', 'experiences', 'resume']

        widgets = {
			'skills': forms.Textarea(attrs={'placeholder': 'Enter your skills'}),
			'qualifications': forms.Textarea(attrs={'placeholder': 'Enter your qualifications'}),
			'experiences': forms.Textarea(attrs={'placeholder': 'Share your experiences'}),
			'resume': forms.FileInput(attrs={'accept':'application/pdf'}),
        }
	
    def clean_category(self):
        category = self.cleaned_data.get('category')

        if not category:
            raise forms.ValidationError("category is required")
        return category

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if not gender:
            raise forms.ValidationError("Gender is required")
        return gender

    def save(self, commit=True):
        user = UserCreationForm.save(self, commit=False)
        user.role = "employee"
        if commit:
            user.save()
        return user


class EmployerRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        UserCreationForm.__init__(self, *args, **kwargs)
        self.fields['gender'].required = True
        self.fields['username'].label = "Username"
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['first_name'].label = "Company Name"
        self.fields['last_name'].label = "Company Address"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"
        self.fields['gender'].label = "Gender"

        self.fields['username'].widget.attrs.update(
            {
                'placeholder': 'Enter Username',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['phoneNumber'].widget.attrs['class'] = 'number'
        self.fields['phoneNumber'].widget.attrs.update(
            {
                'placeholder': 'Enter Phone Number',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )
        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Company Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Company Address',
            }
        )

    class Meta:

        model = User

        fields = ['username',  'email', 'phoneNumber', 'password1', 
			'password2', 'gender', 'first_name', 'last_name',]

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if not gender:
            raise forms.ValidationError("Gender is required")
        return gender

    def save(self, commit=True):
        user = UserCreationForm.save(self, commit=False)
        user.role = "employer"
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Email or username', })
    )
    password = forms.CharField(strip=False, widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
    }))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            if '@' in email:
                usernameStr = str(User.objects.get(email=email).username)
                self.user = authenticate(username=usernameStr, password=password)
            else:
                self.user = authenticate(username=email, password=password)
            try:
                if '@' in email:
                    user = User.objects.get(username=usernameStr)
                else:
                    user = User.objects.get(username=email)
            except User.DoesNotExist:
                raise forms.ValidationError("User Does Not Exist.")

            if not user.check_password(password):
                raise forms.ValidationError("Password Does not Match.")

            if not user.is_active:
                raise forms.ValidationError("User is not Active.")

        return super(UserLoginForm, self).clean(*args, **kwargs)

    def get_user(self):
        return self.user


class EmployeeProfileEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EmployeeProfileEditForm, self).__init__(*args, **kwargs)
		
        profilePicture = forms.ImageField()
        self.fields['username'].widget.attrs.update(
            {
                'placeholder': 'Enter Username',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['phoneNumber'].widget.attrs['class'] = 'number'
        self.fields['phoneNumber'].widget.attrs.update(
            {
                'placeholder': 'Enter Phone Number',
            }
        )
        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Last Name',
            }
        )
		
        skills = forms.Textarea()
        qualifications = forms.Textarea()
        experiences = forms.Textarea()
        resume = forms.FileField()

    class Meta:
        model = User
        fields = ["profilePicture", "username", "email", "phoneNumber", "category", "first_name",
					"last_name", "gender", 'skills', 'qualifications', 'experiences', "resume"]
        widgets = {
			'skills': forms.Textarea(attrs={'placeholder': 'Enter your skills'}),
			'qualifications': forms.Textarea(attrs={'placeholder': 'Enter your qualifications'}),
			'experiences': forms.Textarea(attrs={'placeholder': 'Share your experiences'}),
			'resume': forms.FileInput(attrs={'accept':'application/pdf'}),
        }


class EmployeeChangePassword(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"].widget = forms.PasswordInput(attrs={"class": "form-control"})
        self.fields["new_password1"].widget = forms.PasswordInput(attrs={"class": "form-control"})
        self.fields["new_password2"].widget = forms.PasswordInput(attrs={"class": "form-control"})

		
        self.fields['old_password'].widget.attrs.update(
            {
                'placeholder': 'Enter your old password',
            }
        )
		
        self.fields['new_password1'].widget.attrs.update(
            {
                'placeholder': 'Enter your new password',
            }
        )
		
        self.fields['new_password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm new password',
            }
        )
        # other customization 
