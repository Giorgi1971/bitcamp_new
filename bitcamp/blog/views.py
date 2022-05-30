from dataclasses import field
from distutils.util import execute
from http.server import executable
from django import forms
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, get_list_or_404
from . models import *
from django.db import models
from django.views.generic import (
    CreateView, UpdateView, DeleteView, DetailView, ListView)
from django.urls import reverse_lazy, reverse
from .models import Post
from .forms import CommetModelForm, PostModelForm
from django.contrib.auth import (authenticate, login, logout)
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q


class PostListView(ListView):
    model = Post
    paginate_by = 3

    def get_queryset(self):
        phrase_q = Q()
        q = self.request.GET.get('phrase')
        qa = self.request.GET.get('qa')
        if q:
            phrase_q &= (Q(text__icontains=q) | Q(description__icontains=q) | Q(title__icontains=q))
        if qa:
            phrase_q &= (Q(author__pk=qa))
        return Post.objects.filter(phrase_q).order_by('-pk')


def posts(request):
    phrase_q = Q()
    q = request.GET.get('phrase')
    if q:
        phrase_q &= (Q(text__icontains=q) | Q(description__icontains=q) | Q(title__icontains=q))
    post_list = Post.objects.filter(phrase_q).order_by('-pk')
    paginator = Paginator(post_list, 3)  # Show 3 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog/post_list.html', context)


# ავტომატურად უნდა იყოს ავტორიზებული უსერ პოსტის ავტორი
class PostCreateView(CreateView):
    fields = '__all__'
    model = Post

def post_add(request):
    form = PostModelForm()
    if request.method == 'POST':
        if request.user.is_staff:
            form = PostModelForm(request.POST, request.FILES)
            print(form)
            if form.is_valid():
                postm = form.save(commit=False)
                print(postm)
                # postm.author = request.user.id
                postm.author = Author.objects.get(pk=request.user.pk)
                postm.save()
                # კარგია თუ დამამახსოვრდება, სხვა დროსაც დამჭირდება
                form.save_m2m()
                return redirect(reverse("blog:posts"))
    return render(request, 'blog/post_form.html', {'form':form})


# აქ გვინდა რომ მხოლოდ პოსტის ავტორს შეეძლოს მოხვედრა
class PostUpdateView(UpdateView):
    fields = ('title', 'description', 'text', 'category', 'image')
    model = Post


# ეს არ შლის სურათს მედია ფაილიდან. გადასაწყვეტია ...
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:posts')


class CommentDeleteView(DeleteView):
    model = Comment
    # აქ მირჩევნია იგივე გვერდზე დავრჩე
    success_url = reverse_lazy('blog:posts')
    

def home(request):
    posts = Post.objects.all()[0:10]
    return render(request, 'home.html', {'posts':posts})

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommetModelForm()

    if request.method == 'POST':
        form = CommetModelForm(request.POST)
        if form.is_valid():
            form.instance.post = post
            id = request.POST['id']
            form.instance.author = Author.objects.get(pk=id)
            form.save()
            return redirect(reverse("blog:posts"))
    return render(request, 'blog/post_detail.html', {'post': post, 'com_form':form})


# -----------------------------------------------
# აქედან იქნება Category

class CategoryListView(ListView):
    paginate_by = 3
    model = Category


class CategoryDetailView(DetailView):
    model = Category
