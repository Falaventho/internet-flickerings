from django.db import models
from django.contrib.auth.models import AbstractUser


class FlickerUser(AbstractUser):
    pass

    def __str__(self):
        return self.username
