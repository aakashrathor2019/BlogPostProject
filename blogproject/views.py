from django.shortcuts import render, redirect
from .models import Blog
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import SignupForm, LoginForm, CreatePostForm


class Signup(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')


class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'login.html', {
                    'form': form,
                    'error_message': 'Invalid username or password'
                })
        return render(request, 'login.html', {
            'form': form,
            'error_message': 'Please correct the errors below.'
        })


class Dashboard(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        data = Blog.objects.all()
        print('Dashboard View :', data)
        return render(
            request, 'dashboard.html',
            {'data': data, 'user': request.user})


class CreatePost(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        form = CreatePostForm()
        return render(request, 'createpost.html', {'form': form})

    def post(self, request):
        form = CreatePostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('dashboard')
        return render(request, 'createpost.html', {'form': form})


class Logout(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('login')
