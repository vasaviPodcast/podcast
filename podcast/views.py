from django.shortcuts import render, redirect
from .models import PodcastDetails, User
from .forms import AdminForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound
import os
from django.conf import settings
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.


def download_sqlite(request):
    filepath = os.path.join(settings.BASE_DIR, 'db.sqlite3')
    if os.path.exists(filepath):
        with open(filepath, 'rb') as fh:
            response = HttpResponse(
                fh.read(), content_type="application/x-sqlite3")
            response['Content-Disposition'] = 'inline; filename=' + \
                os.path.basename(filepath)
            return response
    else:
        return HttpResponseNotFound("The requested file does not exist.")


def get_ip(request):
    address = request.META.get("HTTP_X_FORWARDED_FOR")
    if address:
        ip = address.split(",")[-1].strip()
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def get_count(request):
    ip = get_ip(request)
    u = User(user=ip)
    result = User.objects.filter(Q(user__icontains=ip))
    if len(result) == 0:
        u.save()
    count = User.objects.all().count()
    return count


def home(request):
    obj = PodcastDetails.objects.order_by("uploadedOn")
    return render(request, "index.html", {'data': obj, 'visitors': get_count(request)})


def podcast(request, id):
    obj = PodcastDetails.objects.get(id=id)
    return render(request, "song.html", {'data': obj, 'visitors': get_count(request)})


@login_required(login_url='/login')
def adminHome(request):
    records = PodcastDetails.objects.all()
    users = User.objects.all()
    form = AdminForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(adminHome)
    return render(request, "admin.html", {'records': records, 'form': form, 'visitors': get_count(request), 'users': users})


@login_required(login_url='/login')
def update(request, id):
    record = PodcastDetails.objects.get(id=id)
    form = AdminForm(instance=record)
    if request.method == "POST":
        form = AdminForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect(adminHome)
    return render(request, 'update.html', {'data': record, 'form': form})


@login_required(login_url='/login')
def delete(request, id):
    record = PodcastDetails.objects.get(id=id)
    if request.method == "POST":
        response = request.POST["response"]
        if response == "yes":
            record.delete()
        return redirect(adminHome)
    return render(request, "delete.html", {'data': record})


def login(request):
    if request.user.is_authenticated:
        return redirect(adminHome)
    if request.method == "POST":
        uname = request.POST['uname']
        pswd = request.POST['pswd']
        user = authenticate(request, username=uname, password=pswd)
        if user and user.is_superuser:
            auth_login(request, user)
            return redirect(adminHome)
        else:
            return render(request, 'login.html', {'error': True})
    return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return redirect(home)

def feedback(request):
    return render(request,'feedback.html')