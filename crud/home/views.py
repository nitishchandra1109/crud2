from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,redirect
# from django.http import redirect
# relative import of forms
from .models import Employee
from .forms import EmployeeForm

def home_pg(request):
    context = {}
    search = request.GET.get('search')
    if search:
        student = Employee.objects.filter(name = search)
    else:
        student = Employee.objects.all()
    context['stu'] = student
    return render(request, 'show.html' , context)

def create_view(request):
    context = {}
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/list/')
    context['form'] = form

    return render(request, "create_view.html", context)


def list_view(request):
    context = {}
    context["dataset"] = Employee.objects.all()

    return render(request, "list_view.html", context)



def detail_view(request, id):

    context = {}
    context["data"] = Employee.objects.get(id=id)

    return render(request, "detail_view.html", context)


def update_view(request, id):
    context = {}
    obj = get_object_or_404(Employee, id=id)
    form = EmployeeForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/list" )
    context["form"] = form

    return render(request, "update_view.html", context)


def delete_view(request, id):
	context ={}
	obj = get_object_or_404(Employee, id = id)
	if request.method =="POST":
		obj.delete()
		return HttpResponseRedirect("/")

	return render(request, "delete_view.html", context)


