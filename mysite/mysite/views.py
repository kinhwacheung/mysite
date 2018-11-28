from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response
import datetime
# import MySQLdb
from mysite.books.models import Book

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now=datetime.datetime.now()
    return render_to_response('current_datetime.html',{'current_date':now})

def hours_ahead(request,offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()
    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    return render_to_response('hours_ahead.html',{'hour_offset':offset,'next_time':dt})

'''
def book_list(request):
    db=MySQLdb.connect(user='root',passwd='815zhang',host='localhost')
    cursor=db.cursor()
    cursor.excute("SELECT name FROM books ORDER BY name")
    names=[row[0] for row in cursor.fetchall()]
    db.close()
    return render_to_response('book_list.html',{'names':names})
'''
def book_list(request):
    books=Book.objects.order_by('name')
    return render_to_response('book_list.html',{'books':books})


def current_url_view_good(request):
    return HttpResponse("Welcome to the page at {}".format(request.is_secure()))

def display_meta(request):
    values=request.META.items
    return render_to_response('display_meta.html',{'values':values})


#RequestContext和Context处理器
def custom_proc(request):
    return {
            'app':'My app',
            'user':request.user,
            'ip_address':request.META['REMOTE_ADDR']
            }

def view_1(request):
    return renedr_to_response('template1.html',
            {'message':'I am view 1.'},
            context_instance=RequestContext(request,processors=[custom_proc]))

def view_2(request):
    return renedr_to_response('template2.html',
            {'message':'I am view 2.'},
            context_instance=RequestContext(request,processors=[custom_proc]))


