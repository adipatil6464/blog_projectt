from django.http import HttpResponse
from django.shortcuts import render,redirect
from blog.models import *
from django.contrib import messages


def Login(request):
    category = Category.objects.all()
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        category = Category.objects.all()
        if UserAdmin.objects.filter(user_name=user_name).exists():
            obj = UserAdmin.objects.get(user_name=user_name)
            if obj.password == password:
                return redirect('/Admin/',{'category':category})
            else:
                messages.error(request,'wrong password')
                return redirect('/Login/')
        else:
            messages.error(request,'wrong user name')
            return redirect('/Login/')

    return render(request,'login.html',{'category':category})

def home(request):
    category= Category.objects.all()
    post = Post.objects.order_by('?')[:3]
    print(post)
    return render(request,'home.html',{'category':category,'post':post})


def blog(request,url):
    category= Category.objects.all()
    post = Post.objects.get(url=url)
    return render(request,'blog.html',{'category':category,'post':post})


def category(request,url):
    cat = Category.objects.get(url=url)
    category = Category.objects.all()
    post = Post.objects.filter(cat=cat)
    return render(request,'category.html',{'category':category,'post':post,"cat":cat})

def addCategory(request):
    category = Category.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        url = request.POST.get('url')
        image = request.FILES.get('image')  # Use request.FILES to handle file uploads

        c = Category(title=title, description=text, url=url, img=image)
        c.save()
        return render(request, 'addcategory.html', {'category': category})

    return render(request, 'addcategory.html', {'category': category})


def addBlog(request):
    category = Category.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        url = request.POST.get('url')
        cat_id = request.POST.get('cat')
        image = request.FILES.get('image')  # Use request.FILES to handle file uploads

        print(image)
        cat_instance = Category.objects.get(cat_Id=cat_id)

        p = Post(title=title, content=text, url=url, cat=cat_instance, img=image)
        p.save()
        return render(request, 'addblog.html', {'category': category})

    return render(request, 'addblog.html', {'category': category})

        
def Admin(request):
    category = Category.objects.all()
    return render(request,'admin.html',{'category':category})

def About(request):
    return render(request,'about.html')
# Create your views here.
