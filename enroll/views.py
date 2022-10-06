from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
from django.http import JsonResponse
# Create your views here.

def home(request):
  form = StudentRegistration()
  stud = User.objects.all()
  return render(request, 'enroll/home.html', {'form': form, 'stu': stud})

def save(request):
  if request.method == 'POST':
    form = StudentRegistration(request.POST)

    if form.is_valid():
      name = request.POST['name']
      sid = request.POST['stuid']
      email = request.POST['email']
      password = request.POST['password']

      if(sid == ""):
        user = User(name=name, email=email, password=password)
      else:
        user = User(id=sid, name=name, email=email, password=password)

      user.save()

      stud = User.objects.values()
      student_data = list(stud)

      # print(student_data)

      return JsonResponse({'status':'saved', 'student_data':student_data})
    else:
      return JsonResponse({'status':0})


def delete_view(request):
  if request.method == "POST":
    id = request.POST.get('stu_id')
    pi = User.objects.get(pk=id)
    pi.delete()

    return JsonResponse({'status':1})
  else:
    return JsonResponse({'status':0})


def update_view(request):
  if request.method == "POST":
    id = request.POST.get('stu_id')
    student = User.objects.get(pk=id)

    student_data = {
      "id":student.id,
      "name":student.name,
      "email":student.email,
      "password":student.password,
    }
    
    return JsonResponse({'student_data':student_data,'status':1})
  else:
    return JsonResponse({'status':0})