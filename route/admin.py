from django.contrib import admin
from .models import teacher , course ,student ,user_type

admin.site.register(teacher)
admin.site.register(student)
admin.site.register(course)
admin.site.register(user_type)

