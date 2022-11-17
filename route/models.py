from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class teacher(models.Model):
    teacher=models.ForeignKey(User, on_delete=models.CASCADE)


class course(models.Model):
    course_id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=500)
    teacher_name=models.ForeignKey(User, on_delete=models.CASCADE,db_constraint=False)

    def __str__(self):
	    return self.course_name

class student(models.Model):
    student_name=models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(course, on_delete=models.CASCADE,blank=True)


