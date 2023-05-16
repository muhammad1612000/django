from django.shortcuts import render
from .models import Student,course
from .forms import InputForm,StudentForm
# Create your views here.
def list_view(request):
# dictionary for initial data with
# field names as keys
    context ={}
# add the dictionary during initialization
    context["dataset"] = Student.objects.all()
    return render(request, "list_view.html", context)
def list_view1(request):
    context1 ={}
    context1["dataset"] = course.objects.all()
    return render(request, "list_view1.html", context1)

# Create your views here.
def home_view(request):
    context2 ={}
    context2['form']= InputForm()
    return render(request, "home.html", context2)
def home_view2(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
     form.save()
    # save the form data to model
    context3 ={}
    context3['StudentForm']=StudentForm()
    return render(request,"home2.html",context3)