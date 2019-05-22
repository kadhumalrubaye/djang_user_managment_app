from django.contrib import admin
from .models import StudentDegree,Student

# Register your models here.
# .delet sql then migrate then createmigrations then sqlmigrate then createsuperuser
#in case "no such table name" python manage.py makemigrations , python manage.py migrate --run-syncdb
admin.site.register(Student)
admin.site.register(StudentDegree)