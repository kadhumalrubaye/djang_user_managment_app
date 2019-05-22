from django.http import HttpResponse
from django.shortcuts import render
from umapp import models
from umapp import froms

# Create your views here.
def index(request):
    data={'name':'kadhum','age':27,'frinds':['ali','omar','ahmed','jaafar']}
    return render(request,'index.html',data)

def student(request):
    students=models.Student.objects.all()
    context={'students':students}
    return render(request,'student.html',context)

def studentDgree(request,student_id):
    stdegree=models.StudentDegree.objects.filter(student_id=student_id)
    degreeForm = froms.UserDegreeForm(request.POST or None)
    student = models.Student.objects.get(id=student_id)
    if degreeForm.is_valid():
        degree = models.StudentDegree()
        degree.student_id = student
        degree.student_degree = degreeForm.cleaned_data['degree']
        degree.save()
    context = {'dgreeForm': degreeForm,'degree':stdegree}
    return render(request, 'degree.html', context)



def RegesterationFrom(request):
    registerationForm=froms.UserRegisteration(request.POST or None)
    if registerationForm.is_valid():
        msg = 'set'
        student=models.Student()
        student.first_name=registerationForm.cleaned_data['first_name']
        student.last_name=registerationForm.cleaned_data['last_name']
        student.age=registerationForm.cleaned_data['age']
        student.date_birth=registerationForm.cleaned_data['date_birth']
        student.save()
    else:
        msg='not set'

    context={'fromResgester':registerationForm,'msg':msg}
    return render(request,'register.html',context)

# def AddDegree(request,student_id):
#
#     degreeForm=froms.UserDegreeForm(request.POST or None)
#     student=models.Student.objects.get(id=student_id)
#     if degreeForm.is_valid():
#         degree=models.StudentDegree()
#         degree.student_id=student
#         degree.student_degree=degreeForm.cleaned_data['degree']
#         degree.save()
#     context={'dgreeForm':degreeForm}
#     return render(request,'degree.html',context)

