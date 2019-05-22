from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    age=models.IntegerField(default=15)
    date_birth=models.DateField()
    def __str__(self):
        return self.first_name

class StudentDegree (models.Model):

    student_id=models.ForeignKey(Student, on_delete=models.CASCADE)
    student_degree=models.IntegerField(default=15)
    def __str__(self):
        return str(self.student_degree)
