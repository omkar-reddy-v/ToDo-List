from django.shortcuts import render,redirect
from django.http import HttpResponse
from  . models import addtask ,staff
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


@login_required(login_url='signin')
def addtasks(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        date = request.POST.get('date')
        time = request.POST.get('time')
        

        addtask.objects.create(
            task=task,
            date= date,
            time = time,
            uid_id=request.user.id
        )
        messages.add_message(request,messages.SUCCESS,'Task Is Added')
    return render(request,'add.html')

def signup(request):
    if request.method == 'POST':
        fullname  = request.POST.get('fullname')
        email = request.POST.get('email')
        phoneno = request.POST.get('phoneno')
        gender = request.POST.get('gender')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpass = request.POST.get('confirmpass')

        check = User.objects.filter(username = username)
        if len(check)>0:
           return redirect('signup')

        if password == confirmpass:
           user = User.objects.create_user(
               username = username ,
               password= password
           ) 
        # print(username,password)
           staff.objects.create(
                fullname = fullname,
                email = email,
                phoneno = phoneno,
                gender = gender,
                uid_id=user.id
            )   
             

    return render(request,'signup.html')
    


def signin(request):
        if request.method=='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            userdata = authenticate(username = username , password = password)
            if userdata is not None:
                login(request,userdata)
                return redirect('addtaskadd')
        return render(request,'signin.html')


def signout(request):
    logout(request)
    return redirect('signin')

    
@login_required(login_url='signin')
def alltasks(request):
    alltasks=addtask.objects.filter(uid_id=request.user.id)
    return render(request,'alltasks.html',{'alltasks':alltasks})


def edittask(request,id):
    try:
        tasks=addtask.objects.get(id=id)
        if tasks.uid_id!=request.user.id:
            return redirect('edit')
        if request.method == 'POST':
            task = request.POST.get('task')
            date = request.POST.get('date')
            time = request.POST.get('time')

            tasks.task=task
            tasks.date = date
            tasks.time = time
            tasks.save()
            return redirect('alltasks')
        return render(request,'edit.html',{'tasks':tasks})
    except:
        return HttpResponse('<h1>Task is not found</h1>')
def deteleall(request):
    delete = addtask.objects.all()
    delete.delete()
    return redirect('alltasks')

def deleteone(request, id ):
    deleteone = addtask.objects.get(id =id).delete()
    return redirect('alltasks')

