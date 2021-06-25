from django.shortcuts import render , redirect
from .form import EmployeeForm
from .models import Employee

def welcome(request):
    return render(request, "welcome.html")

def  load_form(request):
    form = EmployeeForm
    return render(request, "index.html" , {'form': form })

def add(request):
    form = EmployeeForm(request.POST)
    form.save()    
    return redirect('/show')

def show(request):
    employee = Employee.objects.all
    return render(request, "show.html" , {'employee' : employee})    

def edit(request , id ):
    employee = Employee.objects.get(id=id)
    return render(request, "edit.html" , {'employee' : employee})   

def update(request , id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST , instance=employee)
    form.save()
    return redirect('/show')  

def delete(request , id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')


def serach(request):
    serach_name = request.POST['name']
    employee = Employee.objects.filter(fullname__icontains=serach_name)
    return render(request, "show.html" , {'employee' : employee}) 