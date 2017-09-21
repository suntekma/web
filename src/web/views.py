# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.
# Create your views here.
#from django.template import loader,Context
#from django.http import HttpResponse
#from web.models import BlogPost
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import loader,Context
from django.shortcuts import HttpResponse
from web.models import BlogPost
#def archive(request):
#    posts = BlogPost.objects.all()
#    t = loader.get_template('archive.html')
#    c = Context({'posts': posts})
#    return HttpResponse(t.render(c))

def archive(request):
    blog_list=BlogPost.objects.all()    
    return render_to_response('archive.html',{'blog_list':blog_list})