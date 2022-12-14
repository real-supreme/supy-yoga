from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from asgiref.sync import sync_to_async
from .forms import UsersForm, AuthForm, UserUpdateForm
from asyncio import sleep


def account(request, **kwargs):
    if request.user.is_authenticated:
        return redirect("enroll")
    if kwargs.get("state") is not None:
        state = kwargs.get("state")
    else:
        state = request.GET.get("state", "login")
    print(messages.get_messages(request))
    print(f"state: {state}", request.POST)
    print()
    if request.method == "POST":
        if request.POST.get("age") is None:
            state = "login"
        else:
            state = "register"
    if state == "register":
        if request.method == "POST":
            form = UsersForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your account was created successfully.")
                return redirect("account")
            else:
                messages.error(request, form.errors.as_text())
        else:
            form = UsersForm()
    elif state == "login":
        print("login")
        if request.method == "POST":
            form = AuthForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(
                        request, f"Your login was successful, {user.get_username()}."
                    )
                    return redirect("enroll")
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            form = AuthForm()
    else:
        return render(request, "404.html")
    context = {"form": form, "title": state.capitalize()}
    print(form.fields)
    url = f"/account?state={state}"
    request.session["url"] = url
    return render(request, "register.html", context=context)


def _logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("account")


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {"u_form": u_form, "title": "Profile"}

    return render(request, "users/profile.html", context)


def spechul(request):
    if request.user.is_authenticated:
        return redirect("enroll")
    return render(request, "404.html")


async def login_success(request, *args, **kwargs):
    render(request, "login-success.html")
    await sleep(5)
    return redirect("enroll")
