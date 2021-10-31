from django.forms.utils import to_current_timezone
from django.shortcuts import render,HttpResponseRedirect
from .forms import UserAdminCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import Group
from .models import Book
from .forms import BookForm

# for checking if current user is blongs to particular group




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
            user = form.save()
            group = Group.objects.get(name='Author')
            group.user_set.add(user)
            HttpResponseRedirect('/adminafterlogin/')
            messages.success(request,'Congratulation! You are now regestered as admin')
    return render(request, 'library/adminsignup.html', {'form': form})

def studentsignup_view(request):
    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            group = Group.objects.get(name='Student')
            group.user_set.add(user)
            messages.success(request,'Congratulation! You are now regestered as Student')
    return render(request, 'library/studentsignup.html', {'form': form})


def is_member(user):
    return user.groups.filter(name='Author').exists()

def afterlogin_view(request):
    if request.user.is_authenticated:
        
        books = Book.objects.all()
        
        isadmin = is_member(request.user)
        
        return render(request, 'library/afterlogin.html', {'books': books ,'isadmin':isadmin})
    else:
        return HttpResponseRedirect('/login/')

#Add post
def add_book(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = BookForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = Book(title=title, desc=desc)
                pst.save()
                messages.success(request,'post added succesfully')
                #now passing the empty form after saving post
                form = BookForm()
        else:
            form = BookForm()

        return render(request, 'blog/addpost.html' ,{'form':form})
    else:
        return HttpResponseRedirect('/login/')

#updat post
def update_book(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Book.objects.get(pk=id)
            form = BookForm(request.POST, instance=pi)
            if form.is_valid:
                form.save()
                messages.success(request,'Article Updated succesfully')
        else:
            pi = Book.objects.get(pk=id)
            form = BookForm(instance=pi)

        return render(request, 'library/updatebook.html', {'form': form})
    return HttpResponseRedirect('/login/')

#delete post
def delete_book(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Book.objects.get(pk=id)
            pi.delete()
            messages.success(request, 'Article Deleted succesfully')
        return HttpResponseRedirect('/afterlogin/')
    else:
        return HttpResponseRedirect('/login/')


