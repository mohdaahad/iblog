
import email
from re import search
from turtle import title
from black import json
from django.http import JsonResponse
from django.urls import reverse

from pydoc import text
from django.shortcuts import redirect, render
from .models import Category, Post,activity
from .form import SignUpForm, loginForm, CommentForm
from django.contrib.auth import authenticate,login,logout
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.db.models import Max, Count
from .form import CommentForm,PostForm
from django.shortcuts import render, get_object_or_404
# Create your views here.
def home(request):
    search=1
    if 'search' in request.GET:
        search=request.GET['search']
        post_relevant_title=Post.objects.filter(title__icontains=search)
        post_relevant_cantent=Post.objects.filter(content__icontains=search) 
        post_relevant=post_relevant_title | post_relevant_cantent
    else:
        post_relevant =Post.objects.all()[:11]
    posts=Post.objects.all().order_by('-created_date')
    post_top =Post.objects.all().annotate(count=Count('likes')).order_by('-count')
    
    # print("***************88",post_top)
    cat=Category.objects.all()
    list_of_tuples = [(p,p.comment.count(),p.activity.count()) for p in posts]
    # user=User.objects.get(username=request.user)  
    data ={
        'search':search,
         'cats':cat,
          'posts':list_of_tuples,
        #   'user':user,
          'post_top': post_top,
          'post_relevant': post_relevant,
               }
    return  render(request,'app/home.html',data)
  

def category(request,url):
    cats=Category.objects.all()
    clicked_cat=cats.filter(url=url)
    if 'search' in request.GET:
        search=request.GET['search']
        post_title=Post.objects.filter(title__icontains=search)
        post_cantent=Post.objects.filter(content__icontains=search) 
        posts= post_title | post_cantent
    else:
        posts=Post.objects.filter(category=clicked_cat[0])
    # posts=Post.objects.all().order_by('created_date')[::-1]
    # post_top =Post.objects.all()
    
    return render(request,'app/category.html',{'posts':posts,'cat':clicked_cat[0],'cats':cats})


def user_login(request):
    posts=Post.objects.all()[:11]
    cat=Category.objects.all()
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
                    return HttpResponseRedirect('/')
        else:            
           form = loginForm()
        return render(request,'app/login.html' ,{'form':form ,'post':posts ,'cats':cat })
    else:
        return HttpResponseRedirect('/') 
    

def signup(request):
    posts=Post.objects.all()[:11]
    cat=Category.objects.all()
    if request.method == "POST":
        form=SignUpForm(request.POST)    
        if form.is_valid():
            user =form.save()
            login(request,user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request,'Congratulations!! You have become an authot')
            return HttpResponseRedirect('/')
    else:       
        form=SignUpForm()
    return render(request,'app/signup.html' ,{'form':form ,'post':posts ,'cats':cat})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')        

def about(request):
    posts=Post.objects.all()[:11]
    cat=Category.objects.all()
    return render(request, 'app/about.html' ,{'post':posts ,'cats':cat})

def report(request):
    posts=Post.objects.all()[:11]
    cat=Category.objects.all()
    return render(request, 'app/reportabuse.html' ,{'post':posts ,'cats':cat})
 

def tags(request):
    posts=Post.objects.all()[:11]
    if 'search' in request.GET:
        search=request.GET['search']
        tag_title=Category.objects.filter(title__icontains=search)
        # tag_cantent=Category.objects.filter(description__icontains=search) 
        cat= tag_title
    else:
        cat=Category.objects.all()
    
    return render(request, 'app/tag.html' ,{'post':posts ,'cats':cat})

def contacts(request):
    posts=Post.objects.all()[:11]
    cat=Category.objects.all()
    return render(request, 'app/contacts.html' ,{'post':posts ,'cats':cat})


def post(request,id):
    # posts = get_object_or_404(Post,pk=2)
    post=Post.objects.get(id=id)
    try:
        user=get_object_or_404(User, username=request.user)
        if post.likes.filter(id=user.id).exists():
            likes= 'liked'
            fa_class='fa-solid'

        else:
            likes= 'like'
            fa_class='fa-regular'
    except Exception as e:
        likes= 'like'
        fa_class='fa-regular'
             
    cat=Category.objects.all()
    if 'search' in request.GET:
        search=request.GET['search']
        user_name=post.comment.filter(name__icontains=search)
        comment_text=post.comment.filter(text__icontains=search) 
        comments=user_name | comment_text

    else:
        comments = post.comment.filter()
    new_comment = None
    initial = None
    initial = {'name': request.user.get_username()}
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm(initial=initial)
  
    return render(request,'app/post.html',{
                            # 'user':user,
                            'fa_class':fa_class,
                            'post':post ,'cats':cat,
                            'comments': comments,
                            'likeClass':likes,
                            'new_comment': new_comment,
                            'comment_form': comment_form })

def signout(request):
   posts=Post.objects.all()[:11]
   cat=Category.objects.all()
   return render(request, 'app/logout.html' ,{'post':posts ,'cats':cat})


def likepost(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    user=get_object_or_404(User, username=request.user)
    if post.likes.filter(id=user.id).exists():
        post.likes.remove(user.id)
    else:
        post.likes.add(user.id)
    return JsonResponse({'like':post.likes.count()})
   


def createpost(request):
    user=get_object_or_404(User, id=request.user.id)
    initial={"user_id":user.id}
    if request.method == "POST":
        form=PostForm(request.POST ,request.FILES) 
        print("ye function chala 2")
        print(form.data)
        if form.is_valid():
            print("ye function chala 3")
            form.save()
            return HttpResponseRedirect('/')
    else:       
        form=PostForm(initial=initial)
    return render(request, 'app/createpost.html' ,{'form':form })

def userprofile(request,username):
    user=User.objects.get(username=username)
    cats=Post.objects.all()
    clicked_cat=cats.filter(user_id=user)
    # print(clicked_cat)
    return render(request,"app/userprofile.html",{'user':user , "post":clicked_cat})


def postuserprofile(request,user_id):
    user=User.objects.get(username=user_id)
    cats=Post.objects.all()
    clicked_cat=cats.filter(user_id=user)
    return render(request,"app/postuserprofile.html",{'user':user , "post":clicked_cat})

def editprofile(request):
    user=get_object_or_404(User, username=request.user)
    # print("************************88",user)
    return render(request,'app/editprofile.html',{"user":user})    