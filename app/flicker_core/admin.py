from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import FlickerUserCreationForm, FlickerUserChangeForm
from .models import FlickerUser


class FlickerUserAdmin(UserAdmin):
    add_form = FlickerUserCreationForm
    form = FlickerUserChangeForm
    model = FlickerUser
    list_display = ['email', 'username', ]


admin.site.register(FlickerUser, FlickerUserAdmin)
