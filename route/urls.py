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

]