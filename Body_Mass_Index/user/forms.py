from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class Custom_User_Creation(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class Custom_User_Change(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')
