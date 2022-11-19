from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class teacher(models.Model):
    teacher=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
	    return "teacher_name : " + str(self.teacher)

class course(models.Model):
    course_id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=500)
    teacher_name=models.ForeignKey(User, on_delete=models.CASCADE,db_constraint=False)

    def __str__(self):
	    return "primary key : " + str(self.pk) + " , course_name : " + str(self.course_name)

class student(models.Model):
    student_name=models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(course, on_delete=models.CASCADE,blank=True)

    def __str__(self):
	    return "student_name : " + str(self.student_name)


class user_type(models.Model):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        if self.is_student == True:
            return str(self.user) + " - is_student"
        else:
            return str(self.user) + " - is_teacher"

    def set_teacher(self):
        self.is_teacher=True

    def set_student(self):
        self.is_student=True


