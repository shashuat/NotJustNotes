from django.shortcuts import render ,HttpResponseRedirect , redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as authlogin
from .models import student , course
    

def home(request):
    user = request.user
    if not user.is_authenticated:
        return render(request,'login.html')
    return render(request,"home.html")

def login(request):
    if request.method=='POST':
        user = request.user
        profession=request.POST['profession']
        if profession=="teacher":
            print("teacher")
            return redirect('/teacher/')
        elif profession=="student":
            print("Student")
            return redirect('/student/')
        else:
            return HttpResponseRedirect('')
    return render(request, 'login.html', {})

def teacher_page(request):
    user=request.user
    data=course.objects.filter(teacher_name=user)
    context={"data":data}
    return render(request,'home_teacher.html',context)

def student_page(request):
    user=request.user
    data=student.objects.filter(student_name=user)
    context={"data":data}
    return render(request,'home_student.html',context)
