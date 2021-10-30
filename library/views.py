from django.shortcuts import render,HttpResponseRedirect
from .forms import UserAdminCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

#signup form
def home(request):
    return render(request,"library/home.html")

#for showing signup/login button for student
def studentclick_view(request):
    return render(request,'library/studentclick.html')

#for showing signup/login button for teacher
def adminclick_view(request):
    return render(request,'library/adminclick.html') 

#signup for teacher
def adminsignup_view(request):
    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Congratulation! You are now regestered as admin')
    return render(request, 'library/adminsignup.html', {'form': form})

def studentsignup_view(request):
    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Congratulation! You are now regestered as admin')
    return render(request, 'library/studentsignup.html', {'form': form})

#signup for student
# def studentsignup_view(request):
#     return render(request,'library/studentsignup.html')





