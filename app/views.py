




from django.shortcuts import render
from .models import Category, Post,activity
from .form import SignUpForm, loginForm, CommentForm
from django.contrib.auth import authenticate,login,logout
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    posts=Post.objects.all()[:11]
    cat=Category.objects.all()
    list_of_tuples = [(p,p.comments.filter(likes=1),p.comments.filter(active=True)) for p in posts]
    data ={
         'cats':cat,
          'posts':list_of_tuples,
               }
    return  render(request,'app/home.html',data)
  

def category(request,url):
     cats=Category.objects.all()
     clicked_cat=cats.filter(url=url)
     posts=Post.objects.filter(cat=clicked_cat[0])
    
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
                    return HttpResponseRedirect('/about/')
        else:            
           form = loginForm()
        return render(request,'app/login.html' ,{'form':form ,'post':posts ,'cats':cat})
    else:
        return HttpResponseRedirect('/about/') 
    

def signup(request):
    posts=Post.objects.all()[:11]
    cat=Category.objects.all()
    if request.method == "POST":
        form=SignUpForm(request.POST)    
        if form.is_valid():
            messages.success(request,'Congratulations!! You have become an authot')
            form.save()
            return HttpResponseRedirect('/about/')
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
   



def contacts(request):
    posts=Post.objects.all()[:11]
    cat=Category.objects.all()
    return render(request, 'app/contacts.html' ,{'post':posts ,'cats':cat})


def post(request,url):
    post=Post.objects.get(url=url)
    cat=Category.objects.all()
    comments = post.comments.filter(active=True)
    likes= post.comments.filter(likes=1)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
   
    return render(request,'app/post.html',{
                            'post':post ,'cats':cat,
                            'comments': comments,
                            'likes':likes,
                            'new_comment': new_comment,
                            'comment_form': comment_form })
                            