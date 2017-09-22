from __future__ import unicode_literals
from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from ansible_interface import AnsiInterface
import socket
import iptest.models
from django.http import HttpResponse
import json as simplejson

def index(request):
    return render(request, 'input.html')

def socketport(ip,port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(1)
    try:
        sk.connect((str(ip),port))
        sk.close()
    except Exception as e :
        return e.message
    
def WinorLinux(request):

    ip = request.GET['ip']
    str1=""
    str1 = str(socketport(str(ip),3389))
    if str1 == 'None': 
       data = 'this is windows'    
    elif str1 != 'None':
        str1 = str(socketport(str(ip),22))
        if str1 == 'None': 
            resource = [{"hostname": str(ip), "port": "22", "username": "root", "password": "newegg@123", "ip": '10.16.50.181'}]
            interface = AnsiInterface(resource)
            data = interface.Get_face(['10.16.50.181'])

    # return render_to_response('input.html',{'data':data})
    return HttpResponse(simplejson.dumps(data, ensure_ascii=False))



    
    
    
    
    

    