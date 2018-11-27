from django.shortcuts import render_to_response,render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from mysite.books.models import Book
from mysite.books.forms import ContactForm

# Create your views here.
def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    errors=[]
    if 'q' in request.GET:
        q=request.GET['q']
        if not q:
            errors.append('Please input a search term!')
        elif len(q)>20:
            errors.append('Please enter a term at most 20!')
        else:
            books=Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',{'books':books,'query':q})
    return render_to_response('search_form.html',{'errors':errors})

def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            send_mail(
                    cd['subject'],
                    cd['message'],
                    cd.get('email','1262168096@qq.com'),
                    ['2414400633@qq.com'],
                    )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form=ContactForm(initial={'subject':'I love your site.'})
    return render(request,'contact_form.html',{'form':form})

def thanks(request):
    return HttpResponse("Thanks for your letter!I have already received!")


#create an unusal view
def object_list(request,model):
    obj_list=model.objects.all()
    template_name='%s_list.html'%model.__name__.lower()
    return render_to_response(template_name,{'obj_list':obj_list})


#provide views setting options
def my_view(request,template_name='templates/my_view.html'):
    var=do_something()
    return render_to_response(template_name,{'var':var})


#视图函数高级概念
def method_splitter(request,*args,*kwargs):
    get_view=kwargs.pop('GET',None)
    post_view=kwargs.pop('POST',None)
    if request.method=='GET' and get_view is not None:
        return get_view(request,*args,**kwargs)
    elif request.method='POST' and post_view is not None:
        return post_view(request,*args,**kwargs)
    raise Http404

def some_page_get(request):
    assert request.method=='GET'
    do_something_for_get()
    return render_to_response('page.html')

def some_page_post(request):
    assert request.method=='POST'
    da_something_for_post()
    return HttpResponseRedirect('/someurl')


#包装视图函数
def my_view1(request):
    #
    return render_to_response('template1.html')

def my_view2(request):
    #
    return render_to_response('template2.html')

def my_view3(request):
    #
    return render_to_response('template3.html')

def requires_login(view):
    def new_view(request,*args,**kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login')
        return view(request,*args,**kwargs)
    return new_view


