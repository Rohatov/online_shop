from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from apps.accaunts.form import UserForm
# Create your views here.

class TestView(TemplateView):
    template_name = 'tset.html'


class LoginView(View):
    def get(self, request):
        return render(request, 'page-login-register.html', {})

    def post(self, request):
        phone = request.POST['phone']
        password = request.POST['password']
        user = authenticate(phone=phone, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Succesfully")
            return redirect('products:home')
        messages.error(request, "Incorrect password or phone")
        return render(request, 'page-login-register.html', {})
    

class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.warning(request, "Logout Succesfully")
        return redirect('products:home')


class RegisterView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'register.html', {'form': form})
    
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.data['password1'])
            user.save()
            return redirect('accaunts:login')
        return render(request, 'register.html', {'form': form})