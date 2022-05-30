from re import template
from tkinter.ttk import Widget
from django.db import models
from django.shortcuts import get_object_or_404, render
from django.views.generic import (CreateView, UpdateView, DeleteView, DetailView, ListView)
from django.urls import reverse_lazy, reverse

from blog.models import Post
from .models import Author
from .forms import *
from django.contrib.auth import (authenticate, login, logout)
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.detail import SingleObjectMixin
from django.views import View
from django.http import HttpResponseForbidden, HttpResponseRedirect


def home(request):
    return render(request, 'home.html')


class MentorPostsView(ListView):
    model = Author
    template_name = 'blog/mentor.html'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class AutorListView(ListView):
    queryset = Author.objects.filter(is_staff=True).order_by('?')
    model = Author


class AuthorDetailView(DetailView):
    model = Author


class CreateAuthorView(CreateView):
    fields = ('username', 'first_name', 'last_name', 'image', 'password')
    model = Author


class UpdateAuthorView(UpdateView):
    fields = ('username', 'first_name', 'last_name', 'image')
    model = Author


# ეს არ შლის სურათს მედია ფაილიდან. გადასაწყვეტია ...
class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('user:authors')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = AuthorForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            # user.set_password(user.password1)
            user.save()
            if 'image' in request.FILES:
                user.image = request.FILES['image']
            user.save()
            # Registration Successful!
            registered = True
            return HttpResponseRedirect(reverse('user:login'))
        else:
            print(user_form.errors)
    else:
        user_form = AuthorForm()
    return render(request,'user/author_form.html',
                          {'form':user_form,
                           'registered':registered})


def my_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('blog:home'))
            else:
                # ალბათ ესეც გასასწორებელია.........................................
                return HttpResponse("Your account is not active.")
        else:
            # აქ გასასწორებელია. იგივე გვერდზე უნდა დარჩეს და მესიჯი გამოიტანოს............
            # return HttpResponseRedirect(reverse('blog:home'))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'user/login.html', {})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:home'))