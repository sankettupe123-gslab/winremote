from inspect import trace

from django.shortcuts import render
import winrm
from WinRemote.models import history
from django.utils import timezone
from django.contrib.auth import authenticate
import winrm

def index(request):
    return render(request, 'index.html')

def cmd_input(request):
    try:
        if not request.session['auth']:
            return check_login(request)
        return render(request, "remotecmd.html")
    except Exception:
        return render(request, 'login.html', {'error_message': "enter username and password first."})


def start_login(request):
    request.session['auth'] = False
    return render(request,'login.html')

def check_login(request):
    try:
        username=request.POST['username']
        password=request.POST['passwd']
        user = authenticate(username=username, password=password)
        if user is not None:
                   # the password verified for the user
                   if user.is_active:
                          request.session['auth'] = True
                         # print request.session['auth']
                          print("User is valid, active and authenticated")
                          return render(request, 'index.html')

                   else:
                          return render(request, 'error.html', {'error': "The password is valid, but the account has been disabled!"})
        else:
            return render(request, 'login.html', {'error': "invalid"})

    except ImportError:
        return render(request, 'error.html', {'error': "No reverse match"})

    except UnboundLocalError:
        return render(request, 'error.html', {'error': "Unbound local Error"})

def remote_cmd(request):
    try:
        if not request.session['auth']:
            return check_login(request)

    except Exception:
        return render(request, 'login.html', {'error_message': "enter username and password first."})

    try:
        ip_address = request.POST['ip']
        user = request.POST['user']
        password = request.POST['pass']
        cmd = request.POST['cmd']
        connection = winrm.Session(ip_address, auth=(user,password))
        result = connection.run_ps(cmd)
        #result.status_code
        output = result.std_out
        b = history(command=cmd,output=output,ip=ip_address,time=timezone.now())
        b.save()
        return render(request, 'op.html', {"ip": ip_address,"output": output,"cmd": cmd,"statuscode":result.status_code})
    except Exception as e:
        return render(request, "error.html", {"e": e})

def tools_output(request):
    try:
        if not request.session['auth']:
            return check_login(request)
    except Exception:
        return render(request, 'login.html', {'error_message': "enter username and password first."})

    try:
        ip_address = request.POST['ip']
        user = request.POST['user']
        password = request.POST['pass']
        cmd = request.POST.get('input')
        connection = winrm.Session(ip_address, auth=(user, password))
        result = connection.run_ps(cmd)
        #result.status_code
        output = result.std_out
        b = history(command=cmd, output=output, ip=ip_address, time=timezone.now())
        b.save()
        return render(request, 'op.html',{"ip": ip_address, "output": output, "cmd": cmd, "statuscode": result.status_code})
    except Exception as e:
         return render(request, "error.html", {"e": e})

def startapp_output(request):
    try:
        if not request.session['auth']:
            return check_login(request)

    except Exception:
        return render(request, 'login.html', {'error_message': "enter username and password first."})
    try:
        ipin = request.POST['ip']
        user = request.POST['user']
        passw = request.POST['pass']
        serv = request.POST.get('serv')
        cmd =  request.POST['cmd']
        cmd = serv + " " + cmd
        s = winrm.Session(ipin, auth=(user, passw))
        r = s.run_ps(cmd)
        #r.status_code
        op = r.std_out
        b = history(command=cmd, output=op, ip=ipin, time=timezone.now())
        b.save()
        return render(request, 'op.html', {"ip": ipin,"output": op, "cmd": cmd, "statuscode": r.status_code})
    except Exception as e:
        return render(request, "error.html", {"e": e})


def startapp_input(request):
    try:
        if not request.session['auth']:
            return check_login(request)

    except Exception:
        return render(request, 'login.html', {'error_message': "enter username and password first."})
    return render(request, 'startapp.html')


def tools_input(request):
    try:
        if not request.session['auth']:
            return check_login(request)

    except Exception:
        return render(request, 'login.html', {'error_message': "enter username and password first."})
    return render(request, 'tools.html')


def history_cmd(request):
    try:
        if not request.session['auth']:
            return check_login(request)

    except Exception:
        return render(request, 'login.html', {'error_message': "enter username and password first."})
    all_entries = history.objects.all()
    return render(request, 'history.html',{"obj": all_entries})
