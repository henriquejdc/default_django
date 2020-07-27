from django.shortcuts import render, redirect
from .forms import CustomUserCreateForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from .models import UserDetail, AddressUser


def register(response):
    if response.method == "POST":
        form = CustomUserCreateForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form = CustomUserCreateForm()

    return render(response, "registration/register.html", {"form":form})


class MySignUpView(View):
    form_class = UserCreationForm
    template_name = 'registration/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            u = User.objects.create_user(
                form.cleaned_data.get('username'),
                '',  # request.POST['email'],
                form.cleaned_data.get('password1'),
                is_active=True
            )
            # TODO Display message and redirect to login
            return HttpResponseRedirect('/accounts/login/?next=/')
        return render(request, self.template_name, {'form': form})


def edit_account(request, id):
    ctx = {}
    if UserDetail.objects.filter(user_id=id).exists():
        user = UserDetail.objects.get(user_id=id)
    else:
        user = UserDetail.objects.create(user_id=id)

    if AddressUser.objects.filter(user_detail=id).exists():
        address = AddressUser.objects.get(user_detail=user)
    else:
        address = AddressUser.objects.create(user_detail=user)

    ctx['account'] = user
    ctx['address'] = address
    return render(request, template_name='user/account.html', context=ctx)