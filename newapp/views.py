from django.shortcuts import render,redirect
from .models import Student

# Create your views here.

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_add(request):
    if request.method == 'POST':
        Student.objects.create(
            stud_name = request.POST['stud_name'],
            stud_class = request.POST['stud_class'],
            stud_division = request.POST['stud_division'],
            stud_gender = request.POST['stud_gender'],
            stud_contact = request.POST['stud_contact'],
            stud_place = request.POST['stud_place']
        )
        return redirect('student_list')
    else:
        return render(request, 'student_add.html')
    
def student_update(request, stud_id):
    students = Student.objects.get(stud_id=stud_id)
    if request.method == 'POST':
        students.stud_name = request.POST['stud_name']
        students.stud_class = request.POST['stud_class']
        students.stud_division = request.POST['stud_division']
        students.stud_gender = request.POST['stud_gender']
        students.stud_contact = request.POST['stud_contact']
        students.stud_place = request.POST['stud_place']
        students.save()
        return redirect('student_list')
    return render(request, 'student_update.html', {'student': students})

def student_delete(request, stud_id):
    students = Student.objects.get(stud_id=stud_id)
    students.delete()
    return redirect('student_list')
