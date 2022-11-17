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
    if request.method == "POST":
        c_name=request.POST['name']
        teacher=user
        if user is not None:
            data=course(teacher_name=teacher,course_name=c_name)
            data.save()
            data=course.objects.filter(teacher_name=user)
            context={"data":data}
            return render(request,'home_teacher.html',context)
    else:
        data=course.objects.filter(teacher_name=user)
    context={"data":data}
    return render(request,'home_teacher.html',context)

def student_page(request):
    user=request.user
    if request.method == "POST":
        c_id=course.objects.get(pk=int(request.POST['id']))
        stu=user
        if user is not None:
            data=student(student_name=stu,course_id=c_id)
            data.save()
            data=student.objects.filter(student_name=user)
            context={"data":data}
            return render(request,'home_teacher.html',context)
    else:
        data=student.objects.filter(student_name=user)
    context={"data":data}
    return render(request,'home_student.html',context)
