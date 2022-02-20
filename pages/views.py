from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def full_access_only(view):
    def _decorated(request, *args, **kwargs):
        if not has_full_access(request.user):
            return redirect("no_authorization")
        return view(request, *args, **kwargs)
    return _decorated

def has_full_access(user):
    full_access_users = {'mac': True, 'test_user': False}
    user_name = str(user)
    is_valid = full_access_users.get(user_name, False)
    return is_valid

def no_authorization(request):
    return render(request, "pages/no_authorization.html")

def index(request):
    return render(request, "pages/index.html")

@login_required
@full_access_only
def ftp_view(request):
    return render(request, "pages/ftp.html")

@login_required
def common_view(request):
    return render(request, "pages/common.html")

def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('index')
    return render(request, 'pages/signup.html', {'form': form})
