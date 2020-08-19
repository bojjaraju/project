from django.shortcuts import render
from .forms import student_form
from .models import student
from django.http import HttpResponse
# Create your views here.
def studentinfo(request):
    if request.method=="POST":
        s=student_form(request.POST)
        if s.is_valid():
            s.save()
            return HttpResponse("inserted successfully")
    else:
        s=student_form()
        return render(request,'std_info.html',{'stdinfo':s})

def retreival(request):
    data=student.objects.all()
    return render(request,'result.html',{'records':data})
