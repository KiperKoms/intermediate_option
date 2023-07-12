from django.forms import ModelForm
from .models import Post
from django import forms
from django.contrib.auth.models import Group
from django.db import models
from allauth.account.forms import SignupForm

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'categoryType', 'postCategory', 'title', 'text', 'rating']


class BasicSignupForm(SignupForm):
    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user
