from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import Custom_User_Creation

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = Custom_User_Creation(request.POST)
        if form.is_valid():
            user = from.save()
            login(request, user)
            return redirect('bmi_app:calculate_bmi')
        else:
            from = Custom_User_Creation()
        return render(request, 'signup.html', {'form':form})

@login_required
def daily_check(request):
    if request.method == 'POST':
        height = float(request.POST['height'])
        weight = float(request.POST['weight'])
        bmi = weight / (height ** 2)
        request.user.bmi_history.create(bmi=bmi)
        return redirect('users:daily_check')
    bmi_history = request.user.bmi_history.all().order_by('-date')
    return render(request, 'users/daily_check.html', {'bmi_history': bmi_history})