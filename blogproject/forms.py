from django.contrib.auth.models import User
from .models import Blog
from django import forms


class SignupForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter your password'}),
        label="Password"
    )

    class Meta:
        model = User
        fields = ['username', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Hash the password
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'Enter the post title'}),
            'description': forms.Textarea(
                attrs={'placeholder': 'Enter the post description'}),
        }
