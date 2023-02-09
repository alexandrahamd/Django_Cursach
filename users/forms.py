from django.contrib.auth.forms import UsernameField, UserCreationForm, AuthenticationForm, PasswordResetForm
from users.models import User


class SigninForm(AuthenticationForm):
    pass


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("email",)
        field_classes = {"username": UsernameField}

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.set_password(user.password)
    #     # user.set_password(self.cleaned_data['password'])
    #     if commit:
    #         user.save()
    #     return user


class CustomPasswordResetForm(PasswordResetForm):
    pass