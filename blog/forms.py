from .models import Comment, Post, Photo, User, UserProfile, PhotoProfile
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['description']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('published_date', 'user')


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'


class PhotoProfileForm(forms.ModelForm):
    class Meta:
        model = PhotoProfile
        fields = '__all__'


class UserPhotoChoiceForm(forms.Form):
    use_existing_photo = forms.BooleanField(required=False, initial=True)
    existing_photo = forms.ModelChoiceField(queryset=PhotoProfile.objects.all(), required=False, empty_label="Обери аватар")
    new_photo = forms.ImageField(required=False)


class ProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    use_existing_photo = forms.BooleanField(required=False, initial=True)
    existing_photo = forms.ModelChoiceField(queryset=PhotoProfile.objects.all(), required=False, empty_label="Обери аватар")
    new_photo = forms.ImageField(required=False)
    group = forms.CharField(max_length=30, required=False)
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'use_existing_photo', 'existing_photo', 'new_photo', 'group', 'date_of_birth']


    # def clean(self):
    #     cleaned_data = super().clean()
    #     use_existing_photo = cleaned_data.get('use_existing_photo')
    #     existing_photo = cleaned_data.get('existing_photo')
    #     new_photo = cleaned_data.get('new_photo')
    #
    #     if use_existing_photo and existing_photo is None:
    #         raise forms.ValidationError("Please select an existing photo.")
    #     elif not use_existing_photo and new_photo is None:
    #         raise forms.ValidationError("Please upload your own photo.")
    #
    #     return cleaned_data

class PasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Пароль',
        required=True
    )

    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Новий пароль',
        required=True
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Перевірка нового пароля',
        required=True
    )


class RegistrationForm(UserCreationForm):
    avatar = forms.ImageField(required=False)


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'avatar']
