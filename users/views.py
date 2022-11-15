from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView, View

from .forms import CustomUserCreationForm


class LoginView(TemplateView, View):
    template_name = 'users/login.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})

    def post(self, request, *args, **kwargs):
        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user is not None:
            # the password verified for the user
            if user.is_active:
                login(request, user)
                messages.success(request, "Agora você está logado!")
            else:
                messages.warning(request, "A senha é válida, mas a conta foi desativada!")
        else:
            # the authentication system was unable to verify the username and password
            messages.warning(request, "O nome de usuário e a senha estavam incorretos.")

        return redirect(request.POST.get('next', 'home'))


class LogoutView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('home')

        logout(request)
        messages.success(request, "Você está desconectado agora!")
        return redirect('home')


class RegisterView(TemplateView):
    template_name = 'users/register.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            messages.warning(request, "Você já está logado!")
            return redirect('home')
        return self.render_to_response({'form': CustomUserCreationForm()})

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Já pode iniciar a sessão!")
            return redirect('home')
        else:
            return self.render_to_response({'form': form})


class MembersView(LoginRequiredMixin, TemplateView, View):
    template_name = 'users/members_only.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})
