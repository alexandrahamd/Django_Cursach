from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, TemplateView

from users.models import User


class SigninView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('mysite:messageforsend_list')


class UserProfileView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    fields = ('username', 'email',)
    # form_class = CustomEditUserForm
    success_url = reverse_lazy('mysite:messageforsend_list')

    def get_object(self, queryset=None):
        return self.request.user


class SignupView(CreateView):
    template_name = 'users/register.html'
    model = User
    fields = ('username', 'email', 'password')
    # form_class = SignupForm
    success_url = reverse_lazy('users:register_success')

    # def form_valid(self, form):
    #     if form.is_valid():
    #         self.object = form.save()
    #         set_verify_token_and_send_mail(self.object)
    #     return super().form_valid(form)


class SignupSuccessView(TemplateView):
    template_name = 'users/register_success.html'



