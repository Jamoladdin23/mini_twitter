from django.contrib.auth import login, logout
# from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from users.forms import CustomUser, LoginForm


class RegisterViews(CreateView):
    form_class = CustomUser
    success_url = reverse_lazy('login')
    template_name = 'users/registration.html'


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)  # tut v form berem dannie
        if form.is_valid():  # tut proveril distvitelnost dnnix
            user = form.get_user()  # tut polucil usera
            login(request, user)
            return redirect('post')

    else:
        form = LoginForm()

    return render(request, 'users/login.html', context={'form': form})


def log_out(request):
    logout(request)
    return redirect('logout')


# class UsersListVies(PermissionRequiredMixin):
#     permission_required = 'users.permission_code'
