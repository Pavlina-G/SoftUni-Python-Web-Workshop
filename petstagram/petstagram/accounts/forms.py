from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class UserCreateForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email')
        field_classes = {
            'username': auth_forms.UsernameField,
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username: ',
                },
            ),
        }


class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        # fields = ('first_name',)
        fields = "__all__"
        field_classes = {'username': auth_forms.UsernameField}