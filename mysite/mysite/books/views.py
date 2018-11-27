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
def my_view(request,template_name):
    var=do_something()
    return render_to_response(template_name,{'var':var})



