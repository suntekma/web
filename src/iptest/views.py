from __future__ import unicode_literals
from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
import socket


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
       str1 = 'this is windows'    
    elif str1 != 'None':
        str1 = str(socketport(str(ip),22))
        if str1 == 'None': 
            str1 = 'this is linux'
                
    
    return render_to_response('input.html',{'str1':str1})

    
    
    
    
    

    