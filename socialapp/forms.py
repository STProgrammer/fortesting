from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form with Bootstrap styling."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class BootstrapUserCreationForm(UserCreationForm):
    """User creation form with Bootstrap styling."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields
