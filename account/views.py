from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login , logout


def Singup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/')
    form = UserCreationForm()
    return render(request, 'account/singup.html',{'form' : form})

def Login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('/')

    form = AuthenticationForm()
    return render(request, 'account/login.html', {'form':form})


def Logout_view(request):
   if request.method == 'POST':
        logout(request)
        return redirect('/')
