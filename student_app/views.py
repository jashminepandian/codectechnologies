from django.shortcuts import render, redirect
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_app/list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST['name'],
            roll_number=request.POST['roll_number'],
            email=request.POST['email'],
            course=request.POST['course']
        )
        return redirect('student_list')
    return render(request, 'student_app/form.html')

def student_update(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.roll_number = request.POST['roll_number']
        student.email = request.POST['email']
        student.course = request.POST['course']
        student.save()
        return redirect('student_list')
    return render(request, 'student_app/form.html', {'student': student})

def student_delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_list')
