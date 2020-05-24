from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegisterForm


def register(request):
    if request.user.is_authenticated:
        return redirect(reverse("index"))

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


@login_required
def profile(request):
    if request.user.is_authenticated is False:
        messages.error(
            request, "You are not authenticated, please login to view this page"
        )
        return redirect("login")
    return render(request, "profile.html")
