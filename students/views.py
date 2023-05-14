from django.shortcuts import render
from .models import Student,course
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