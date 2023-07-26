from django.shortcuts import render, redirect
from .models import Registration,Document
from django.http import HttpResponse
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.


def index(request):
    form = Registration.objects.all()
    return render(request, 'index.html', {'form': form})


def login(request):
    return render(request, 'login.html')


def registration(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        company = request.POST['company']
        password = make_password(request.POST['password'])
        if Registration.objects.filter(Email=email).exists():
            return render(request, 'index.html', {'msg': 'email already'})
        elif Registration.objects.filter(Phone=phone).exists():
            return render(request, 'index.html', {'msg': 'phone already'})
        else:
            Registration.objects.create(
                Name=name, Phone=phone, Email=email, Password=password, Company=company)
            return redirect('/login/')
    else:
        return HttpResponse('Email is not register')


# def log(request):
#     if request.method == 'POST':


def table(request):
    form=Document.objects.all()
    return render(request, 'table.html',{'form':form})


def delete(request, id):
    Registration.objects.get(id=id).delete()
    return redirect('/table/')


def login_data(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        if Registration.objects.filter(Email=email).exists():
            user_obj = Registration.objects.get(Email=email)
            user_password = user_obj.Password
            if check_password(password, user_password):
                return redirect('/profile/')
            else:
                return render(request, 'login.html', {'msg': 'Password Incorrect'})
        else:
            return render(request, 'login.html', {'msg': 'Email Incorrrect'})
        
def profile(request):
    form=Document.objects.all()
    return render(request,'profile.html',{'form':form})

def profile_data(request):
    if request.method == 'POST':
        pp=request.FILES.get('ppn')
        ac=request.FILES.get('acn')
        pc = request.FILES.get('pan')
        vip=request.FILES.get('vipn')
        ms=request.FILES.get('msn')
        Document.objects.create(pp=pp,ac=ac,pc=pc,vip=vip,ms=ms)
        return redirect('/table/')
    else:
        return render(request,'profile.html')
    

def success(request):
    return render(request,'success.html')


