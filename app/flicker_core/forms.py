from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import FlickerUser


class FlickerUserCreationForm(UserCreationForm):

    class Meta:
        model = FlickerUser
        fields = ('username', 'email')


class FlickerUserChangeForm(UserChangeForm):

    class Meta:
        model = FlickerUser
        fields = ('username', 'email')
