from django.shortcuts import render, reverse, HttpResponseRedirect
from .models import Student
from .forms import StudentForm

# Create your views here.
def home(request):
    student = Student.objects.all()

    context={
        "students" : student,
    }
    return render(request,"home/index.html",context)

def postView(request, id):
  student = Student.objects.get(pk=id)
  contaxt ={
      "students": student,
  }
  return render(request, 'home/postView.html',contaxt)


def add(request):
    if request.method == 'POST':
        form= StudentForm(request.POST)
        if form.is_valid():
            NewStudentNumber = form.cleaned_data['studentNumber']
            NewFirstName = form.cleaned_data['firstName']
            NewLastName = form.cleaned_data['lastName']
            NewEmail = form.cleaned_data['email']
            NewStudyField = form.cleaned_data['studyField']
            Newgpa = form.cleaned_data['gpa']

            NewStudent = Student(
                studentNumber= NewStudentNumber,
                firstName= NewFirstName,
                lastName= NewLastName,
                email= NewEmail,
                studyField= NewStudyField,
                gpa = Newgpa
            )
            NewStudent.save()
            context = {
                'form': form,
                'success': True,
            }
            return render(request,'home/add.html',context)
    else:
        form = StudentForm()
        context = {
            'form': form,            }
    return render(request,'home/add.html',context)

def edit(request, id):
    if request.method == "POST":
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
            'success': True,
        }
        return render(request,'home/edit.html',context)
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
        context = {
            'form': form,
        }
    return render(request,'home/edit.html',context)

def delete(request, id):
    #if request.method == "POST":
    student = Student.objects.get(pk=id)
    student.delete()
    return HttpResponseRedirect(reverse('index'))
