from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UpdateUserForm(forms.ModelForm):
    phone = forms.CharField(max_length=15, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'address', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            try:
                user_profile = self.instance.profile
                self.fields['phone'].initial = user_profile.phone
                self.fields['address'].initial = user_profile.address
                self.fields['image'].initial = user_profile.image
            except Profile.DoesNotExist:
                pass

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user_profile, created = Profile.objects.get_or_create(user=user)
            user_profile.phone = self.cleaned_data['phone']
            user_profile.address = self.cleaned_data['address']
            if self.cleaned_data['image']:
                user_profile.image = self.cleaned_data['image']
            user_profile.save()
        return user