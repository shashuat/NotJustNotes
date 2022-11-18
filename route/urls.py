from django.urls import path , include
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.login,name="login"),
    path('accounts/', include('allauth.urls')),
    path('logout/', LogoutView.as_view()),
    path('teacher/', views.teacher_page,name="teacher"),
    path('student/', views.student_page,name="student"),
    path('classroom/<str:pk>/student/', views.student_classroom,name="student-class"),
    path('classroom/<str:pk>/teacher/', views.teacher_classroom,name="teacher-class"),

]