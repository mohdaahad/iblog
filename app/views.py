




from django.shortcuts import render
from .models import Category, Post
from .form import SignUpForm, loginForm
from django.contrib.auth import authenticate,login,logout
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.
def home(request):
     posts=Post.objects.all()[:11]
     cat=Category.objects.all()
    #  print("*************",cat[0].color)
     data ={
         'cats':cat,
          'posts':posts
     }
     return  render(request,'app/home.html',data)

def post(request,url):
     post=Post.objects.get(url=url)
     cat=Category.objects.all()
     return render(request,'app/post.html',{'post':post ,'cats':cat})


def category(request,url):
     cats=Category.objects.all()
     clicked_cat=cats.filter(url=url)
     posts=Post.objects.filter(cat=clicked_cat[0])
    
     return render(request,'app/category.html',{'posts':posts,'cat':clicked_cat[0],'cats':cats})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = loginForm(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass =form.cleaned_data['password']
                user =   authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Successfuly!!!')
                    return HttpResponseRedirect('/about/')
        else:            
           form = loginForm()
        return render(request,'app/login.html' ,{'form':form})
    else:
        return HttpResponseRedirect('/about/') 
    

def signup(request):
  
    if request.method == "POST":
        form=SignUpForm(request.POST)    
        if form.is_valid():
            messages.success(request,'Congratulations!! You have become an authot')
            form.save()
            return HttpResponseRedirect('/about/')
    else:        
        form=SignUpForm()
    return render(request,'app/signup.html' ,{'form':form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')        

def about(request):
    return render(request, 'app/about.html')

def report(request):
    return render(request, 'app/reportabuse.html')



def contacts(request):
    return render(request, 'app/contacts.html')