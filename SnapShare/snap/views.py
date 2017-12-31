# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import User, Post
from django.views.generic import View
from .forms import UserForm, PostForm


class HomeView(generic.ListView):
    template_name = "snap/home.html"

    def get_queryset(self):
        return Post.objects.all()

class DetailView(generic.DetailView):
    model = Post
    template_name = "snap/detail.html"

#
# def post_create(request):
#     form = PostForm(request.POST or None)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save()
#
#     context = {
#         "form": form
#     }
#     return render(request, "snap/post_form.html", context)

class PostCreate(CreateView):
    template_name = 'snap/post_form.html'
    form_class = PostForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.save()





# class PostCreateNew(CreateView):
#     template_name = 'snap/post_form.html'
#     model = Post
#     form = PostForm()
#     # fields = ['user', 'likes', 'image', 'comment']
#
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save()



    # def form_valid(self, form):
    #     self.object = form.save(commit=False)  # Not hit database
    #     self.object.user = self.request.user  # Update user
    #     self.object.post_date = datetime.now()  # Update post_date
    #     self.object.save()  # And finally save your object to database.


class RegisterFormView(View):
    form_class = UserForm
    template_name = "snap/register.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("snap : home.html")

        return render(request, self.template_name, {"form": form})

class LoginFormView(View):
    form_class = UserForm
    template_name = "snap/login.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("snap : home.html")

        return render(request, self.template_name, {"form": form})
# Create your views here.
