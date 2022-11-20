from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from route import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('route.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),

]
