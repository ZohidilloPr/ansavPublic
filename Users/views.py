from .models import UserProfile
from .forms import NewUserForm, UpdateProfileForm, UpdateUserForm
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def Profile(request):
    if request.user.is_authenticated:
        user = request.user
        user, created = UserProfile.objects.get_or_create(user=user)
    return render(request, 'pages/UserHome.html')


def SignUp_function(request):
    if request.user.is_authenticated:
        user = request.user
        user, created = UserProfile.objects.get_or_create(user=user)
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Ro\'yhatdan o\'tish muaffaqiyatli yakunlandi!')
            return redirect('Users:Profile')
        else:
            messages.error(request, f'Kiritilgan malumotlaringizni tekshirib yana bir marta kiriting!')
    form = NewUserForm
    return render(request, 'register/signup.html', context={'form':form})            

def LogIn_function(request):
    if request.user.is_authenticated:
        user = request.user
        user, created = UserProfile.objects.get_or_create(user=user)
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Profilga kirish muaffaqiyatli yakunlandi!')
                return redirect('Users:Profile')
            else:
                messages.error(request, 'username yoki password da xatolik bor tekshirib boshqatdan kiriting!')
        else:
            messages.error(request, 'username yoki password da xatolik bor tekshirib boshqatdan kiriting!')
    form = AuthenticationForm
    return render(request, 'register/login.html', context={'login_form':form})                    

def Logout_function(request):
    logout(request)
    messages.info(request, 'Xayr :( ')
    return redirect('Ads:Home')

def Update_function(request):
    if request.method == 'POST':
        uform = UpdateUserForm(data=request.POST, instance=request.user)
        pform = UpdateProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            messages.success(request, 'Profilingiz Muaffaqiyatli Yangilandi!')
            return redirect('Users:Profile')
    else:
        uform = UpdateUserForm(instance=(request.user))
        pform = UpdateProfileForm(request.FILES, instance=(request.user.userprofile))
    context = {
        'uform':uform,
        'pform':pform,
    }
    return render(request, 'pages/update.html', context)