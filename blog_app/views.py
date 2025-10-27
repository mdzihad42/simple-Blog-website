from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from blog_app.models import*

def registerPage(request):
    if request.method=="POST":
        full_name=request.POST.get('full_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        user_type=request.POST.get('user_type')
        user_exists=UserInfoModel.objects.filter(username=username).exists()
        if user_exists:
            return redirect('registerPage')
        if password==confirm_password:
            UserInfoModel.objects.create_user(
                full_name=full_name,
                username=username,
                email=email,
                password=password,
                user_type=user_type
            )
            return redirect('loginPage')
    return render(request,'auth/register.html')
def loginPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('homePage')
    return render(request,'auth/login.html')
def logoutPage(request):
    logout(request)
    return redirect('loginPage')
@login_required
def addPage(request):
    if request.method=="POST":
        title=request.POST.get('title')
        content=request.POST.get('content')
        category=request.POST.get('category')
        image=request.FILES.get('image')
        published_date=request.POST.get('published_date')
        PostModel(
            title=title,
            content=content,
            category=category,
            status= 'Pending',
            image=image,
            published_date=published_date,
            created_by=request.user
        ).save()
        return redirect('postPage')
    return render(request,'post/addpost.html')
@login_required
def postPage(request):
    if request.user.user_type == 'Admin':
        post=PostModel.objects.all()
    else:
        post=PostModel.objects.filter(created_by=request.user)
    context={
        'post':post
    }
    return render(request,'post/post.html',context)
@login_required
def postDlt(request,id):
    PostModel.objects.get(id=id).delete()
    return redirect('postPage')
@login_required
def postEdit(request,id):
    post_data=PostModel.objects.get(id=id)
    if request.method=="POST":
        title=request.POST.get('title')
        content=request.POST.get('content')
        category=request.POST.get('category')
        image=request.FILES.get('image')
        published_date=request.POST.get('published_date')
        if image:
            post_data.image=image
        post_data.title=title
        post_data.content=content
        post_data.category=category
        post_data.published_date=published_date
        post_data.created_by=request.user
        post_data.save()
        return redirect('postPage')
    return render(request,'post/postEdit.html',{'post_data':post_data})
@login_required
def pending_status(request,id):
    post=PostModel.objects.get(id=id)
    if post.status == 'Reject':
        post.status = 'Pending'
    elif post.status == 'Publish':
        post.status = 'Reject'
    post.save()
    return redirect('postPage')
@login_required
def publish_status(request,id):
    post=PostModel.objects.get(id=id)
    if post.status == 'Pending':
        post.status = 'Publish'
    elif post.status == 'Reject':
        post.status = 'Publish'
    post.save()
    return redirect('postPage')

@login_required
def reject_status(request,id):
    post=PostModel.objects.get(id=id)
    if post.status == 'Pending':
        post.status = 'Reject'
    elif post.status == 'Publish':
        post.status = 'Reject'
    post.save()
    return redirect('postPage')

@login_required
def homePage(request):
    if request.user.user_type == 'Admin':
        post=PostModel.objects.all()
    else:
        post=PostModel.objects.filter(created_by=request.user)
    context={
        'post':post
    }
    return render(request,'master/base.html',context)