from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from .models import Profile

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            Profile.objects.create(
                user=user,
                notes=form.cleaned_data.get("notes", ""),
                first_name=form.cleaned_data["first_name"],
                surname=form.cleaned_data["surname"],
                gender=form.cleaned_data["gender"],
                date_of_birth=form.cleaned_data.get("date_of_birth"),
                address=form.cleaned_data["address"],
                suburb=form.cleaned_data["suburb"],
                postcode=form.cleaned_data["postcode"],
                state=form.cleaned_data["state"],
                phone_number=form.cleaned_data.get("phone_number", ""),
            )

            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})
