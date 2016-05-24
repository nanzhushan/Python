#coding:utf8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect

from django.template import RequestContext


# Create your views here.


#http://127.0.0.1:8000/get/?a=5
def get(request):
    a = request.GET['a']
    b = request.GET['b']
    # b = u"哈哈"+ a
    c = a + "..."+ b
    f = open("d:\\get.txt",'a')
    f.write(c)
    f.write("\n")
    f.close
    return HttpResponse(c)

