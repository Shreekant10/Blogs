from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


from .models import Post, Category, Tags    



def register_user(request):
    if request.method == "POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        username = request.POST['username']
        # number = request.POST['phone_number']
        email = request.POST['email_id']
        pass1 = request.POST['pass1']
        cnf_pass = request.POST['pass2']
        
        
        # validation
        # if len(username) < 10:
        #     messages.error(request, "Your username must be below 10 character")
        #     return redirect('/user/register')
        
        # if not username.islanum():
        #     messages.error(request, "Your username should contain letters and numbers")
        #     return redirect('/user/register')
        
        if (pass1 != cnf_pass):
            messages.warning(request, "Password and Confirm Password didn't matched")
            return redirect('register_url')
        
        
        # saving user data
        user = User.objects.create_user(username, email, password = cnf_pass)
        user.first_name = fname
        user.last_name = lname
        user.save()
        messages.success(request, "Your Account has been Successfully Created")
        return redirect('login_url')  
    return render(request, 'auth/register.html')



def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['pass1']
        
        # Authenticate
        user = authenticate(request, username = username, password = password)
        if user is None:
            messages.warning(request, "There was an error logging in, Please try again...")
            # return redirect('/user/login')
            return redirect('login_url')
        else:
            login(request, user)
            messages.success(request, "Successfully Logged In!")
            return redirect('index')
        
        
        # if user is not None:
        #     login(request, user)
        #     messages.success(request, "You have been logged in!")
        #     return redirect('index')
        # else:
        #     messages.warning(request, "There was an error logging in, Please try again...")
        #     return redirect('/user/login')
    else:
        return render(request, 'auth/login.html')



def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out !")
    return redirect('index')



def index(request):
    categories = Category.objects.all()
    popular_post = Post.objects.filter(section = 'Popular').order_by('-id')[0:4]
    recent_post = Post.objects.filter(section = 'Recent').order_by('-id')[0:4]
    main_post = Post.objects.filter(main_post = True)[0:1]
    editors_pick = Post.objects.filter(section = 'Editors_Pick').order_by('-id')
    trending = Post.objects.filter(section = 'Trending').order_by('-id')
    # single_post = Post.objects.get(slug = slug, status = 'published')
    # print(post)
    
    context = {
        'categories' : categories,
        'popular_post' : popular_post,
        'recent_post' : recent_post,
        'main_post' : main_post,
        'editors_pick' : editors_pick,
        'trending' : trending,
        # 'single_post' : single_post
    }
    return render(request, 'main/index.html', context)




def post_by_category(request, category_name):
    categories = Category.objects.all()
    category_post = Post.objects.filter(category__name = category_name, status = 'published').order_by('-id')
    print('category name : ', category_name)
    context = {
        'category_name' : category_name,
        'categories' : categories,
        'category_post' : category_post
    }
    return render(request, 'main/post_by_category.html', context)




def single_post(request, slug):
    single_post = Post.objects.get(slug = slug, status = 'published')
    # print('single post :', single_post)
    context = {
        'single_post' : single_post
    }
    return render(request, 'main/blog_single_alt.html', context)




def search(request):
    keyword = request.GET.get('keyword')
    blogs = Post.objects.filter(title__icontains = keyword)
    # print(blogs)
    context = {
        'blogs' : blogs
    }
    return render(request, 'main/search.html', context)

