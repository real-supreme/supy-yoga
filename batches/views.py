from django.shortcuts import render, redirect
from asgiref.sync import sync_to_async
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BatchForm


@login_required
def enroll(request):
    if request.method == "POST":
        form = BatchForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account was created successfully.")
            return redirect("profile")
        else:
            messages.error(request, form.errors.as_text())
    else:
        form = BatchForm()
    context = {"form": form, "title": "Enrollment"}
    return render(request, "enroll.html", context=context)


def account(request, *args, **kwargs):
    return redirect("account", request, *args, **kwargs)
