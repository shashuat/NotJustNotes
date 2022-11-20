from django.shortcuts import render ,HttpResponseRedirect , redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as authlogin
from .models import student , course , user_type
from django.contrib import messages

def login(request):
    return render(request, 'login.html', {})


def select_profession(request):
    user=request.user
    try:
    #if user_type.objects.get(user=user).exists():
        obj=user_type.objects.get(user=user)
        if obj.is_student==True or obj.is_teacher==True:
            if obj.is_teacher==True:
                return redirect('/teacher/')
            else:
                return redirect('/student/')
    except user_type.DoesNotExist:
        if request.method=='POST':
            job=request.POST['profession']   
            if job=="teacher":
                data=user_type(is_teacher=True,is_student=False,user=user)
                data.save()
                print("teacher")
                return redirect('/teacher/')
            elif job=="student":
                data=user_type(is_teacher=False,is_student=True,user=user)
                data.save()
                print("Student")
                return redirect('/student/')
            else:
                return HttpResponseRedirect('')
            
    context={}
    return render(request,"select-job.html",context)

def teacher_page(request):
    user=request.user
    obj=user_type.objects.get(user=user)
    if obj.is_student==False and obj.is_teacher==True:
        if request.method == "POST":
            c_name=request.POST['name']
            teacher=user
            if not course.objects.filter(course_name=c_name).exists():
                data=course(teacher_name=teacher,course_name=c_name)
                data.save()
                messages.success(request, f'new course {c_name} created successfully')
                data=course.objects.filter(teacher_name=user)
                context={"data":data}
                return render(request,'home_teacher.html',context)
        else:
            data=course.objects.filter(teacher_name=user)
        data=course.objects.filter(teacher_name=user)
        context={"data":data}
        return render(request,'home_teacher.html',context)
    else:
        return render(request,'error.html')

def student_page(request):
    user=request.user
    obj=user_type.objects.get(user=user)

    if obj.is_student==True and obj.is_teacher==False:
        if request.method == "POST":
            c_id=course.objects.get(pk=int(request.POST['id']))
            stu=user
            if not student.objects.filter(course_id=c_id).exists():
                data=student(student_name=stu,course_id=c_id)
                data.save()
                messages.success(request, 'New course added succcessfully')
                data=student.objects.filter(student_name=user)
                context={"data":data}
                return render(request,'home_teacher.html',context)
        else:
            data=student.objects.filter(student_name=user)
        data=student.objects.filter(student_name=user)
        context={"data":data}
        return render(request,'home_student.html',context)
    else:
        return render(request,'error.html')


def student_classroom(request,**kwargs):
    user=request.user
    obj=user_type.objects.get(user=user)
    if obj.is_student==True and obj.is_teacher==False:
        pk=kwargs.get('pk')
        context={"pk":pk}
        return render(request,"classroom-student.html",context)
    else:
        return render(request,'error.html')

def teacher_classroom(request,**kwargs):
    user=request.user
    obj=user_type.objects.get(user=user)
    if obj.is_student==False and obj.is_teacher==True:
        pk=kwargs.get('pk')
        context={"pk":pk}
        return render(request,"classroom-teacher.html",context)
    else:
        return render(request,'error.html')

