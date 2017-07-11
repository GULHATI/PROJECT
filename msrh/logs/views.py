#log/views.py
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from msrh_user.models import HR,HOD,SUPERVISOR,EMPLOYEE, Training, DEPARTMENT, Pending_Trainings , Names
from django.db.models import Q
# Create your views here.
# this login required decorator is to not allow to any
# view without authenticating

check = "false"
y = HOD.objects.all()
k = HR.objects.all()
a = SUPERVISOR.objects.all()
u = EMPLOYEE.objects.all()
l = DEPARTMENT.objects.all()
r = Training.objects.all()

@login_required(login_url="login/")
def home(request):
    z = 0
    for x in y :
        if(x.Eid == request.user.username):
            z=1
            HOD_name=x.name
            HOD_Eid=x.Eid
            HOD_dept=x.department
            HOD_pos=x.position
            return render(request, "hod_home.html", {'HOD_name': HOD_name, 'HOD_Eid': HOD_Eid, 'HOD_dept': HOD_dept, 'HOD_pos': HOD_pos})
    if z == 0:
        for x in k :
            if(x.Eid == request.user.username):
                z=1
                HR_name=x.name
                HR_Eid=x.Eid
                HR_dept=x.department
                HR_pos=x.position
                return render(request,"hr_home.html",{'HR_name': HR_name, 'HR_Eid': HR_Eid, 'HR_dept': HR_dept, 'HR_pos': HR_pos})
    if z == 0:
        for x in a:
            if (x.Eid == request.user.username):
                z = 1
                Sup_name=x.name
                Sup_Eid=x.Eid
                Sup_dept=x.department
                Sup_pos=x.position
                return render(request, "supervisor_home.html",{'Sup_name': Sup_name, 'Sup_Eid': Sup_Eid, 'Sup_dept': Sup_dept, 'Sup_pos': Sup_pos})
    if z == 0:
            return render(request, "login.html")

@login_required(login_url="login/")
def test(request):
    return render(request, "test.html", {'accept': u})

@login_required(login_url="login/")
def maketraining(request):
    return render(request, "maketraining.html", {'dept':l})


def make(request):
    if request.method == "POST":
        train = Training()
        dept = DEPARTMENT()
        train.name = request.POST['tname']
        train.venue = request.POST['tvenue']
        train.date = request.POST['tdate']
        train.time = request.POST['ttime']
        dept.name = request.POST['tdept']
        train.department = dept
        train.topic = request.POST['ttopic']
        train.head_of_program = request.POST['thead']
        train.save()
        check = "true"
        return render(request, "maketraining.html",{'check': check, 'dept':l})


def shows(request):
    return render(request, "show.html", {'train':r})


def request_training(request):
    name = request.user.username
    d = HOD.objects.filter(Eid=name).values_list('department')
    e = EMPLOYEE.objects.filter(Q(department=d))
    return render(request, "request_training.html", {'dept': l, 'train': r, 'emp': e})


def req_training(request):
   if request.method == "POST":
        pending = Pending_Trainings()
        names=Names()
        pending.name = request.POST['tname']
        pending.dept = request.POST['tdept']
        pending.emp_count = request.POST['emp_count']

        emp_list = request.POST.getlist('emp')
        for hola in emp_list:
            names.name=hola
            names.save()
            pending.save()
            pending.emp_list.add(names)
        pending.save()
        return HttpResponse("ADDED TO PENDING LIST")


def pending(request):
    t = Pending_Trainings.objects.all()
    return render(request,"pending.html",{'pending': t})

def apply(request):
    if request.method == "POST":
        x = request.POST['name']
        return render(request,"gogog.html",{'gogog':x})
    return HttpResponse("ghn")
