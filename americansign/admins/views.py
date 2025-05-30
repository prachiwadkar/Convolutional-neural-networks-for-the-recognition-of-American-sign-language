from django.shortcuts import render
from user.models import userregistration
from django.contrib import messages
# Create your views here.
def adminlogin(request):
    return render(request,'adminlogin.html')

def adminbase(request):
    return render(request,'admins/adminbase.html')

def users(request):
    users = userregistration.objects.all()
    return render(request,'admins/users.html',{'users':users})

def menu(request):
    return render(request,'admins/menu.html')

def AdminLoginCheck(request):
    if request.method == 'POST':
        usrid = request.POST.get('loginname')
        pswd = request.POST.get('pswd')
        print("User ID is = ", usrid)
        if usrid == 'admin' and pswd == 'admin':
            return render(request, 'admins/adminbase.html')
        elif usrid == 'Admin' and pswd == 'Admin':
            return render(request, 'admins/adminbase.html')
        else:
            messages.success(request, 'Please Check Your Login Details')
    return render(request, 'admin.html', {})

def AdminActivaUsers(request):
    if request.method == 'GET':
        id = request.GET.get('uid')
        status = 'activated'
        print("PID = ", id, status)
        userregistration.objects.filter(id=id).update(status=status)
        data = userregistration.objects.all()
        print(data)
        return render(request, 'admins/Users.html', {'users': data})

