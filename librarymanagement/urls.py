"""librarymanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from library import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('adminclick/',views.adminclick_view),
    path('studentclick/',views.studentclick_view),

    path('adminsignup/', views.adminsignup_view,name='adminsignup'),
    path('adminlogin/', LoginView.as_view(template_name='library/adminlogin.html'),name='adminlogin'),
    path('studentsignup/', views.studentsignup_view,name='studentsignup'),
    path('studentlogin/', LoginView.as_view(template_name='library/studentlogin.html'),name='studentlogin'),
    
]
