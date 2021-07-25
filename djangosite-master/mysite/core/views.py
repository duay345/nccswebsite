from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import CommentForm
from django.shortcuts import render, get_object_or_404


from .forms import infoForm
from .forms import IntroForm
from .forms import mydocForm
from .forms import profileForm
from .forms import skillsForm
from .forms import AboutyouForm

from .models import info
from .models import Intro
from .models import mydoc
from .models import profile
from .models import skills
from .models import Comment
from .models import Aboutyou

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy


class Home(TemplateView):
    template_name = 'home.html'

def common(request):
    return render( request,'common.html',{})

def forminfo(request):
    return render( request,'forminfo.html',{})

def header(request):
    return render(request, 'header.html',{})



def post_detail(request):
    comm = 'comm.html'
    post = get_object_or_404(skills)
    comments = post.comments.filter(active=True)
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

    return render(request, comm, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

def upload_mydoc(request):

    if request.method == 'POST':
        form = mydocForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('skills')
    else:
        form = mydocForm()
    return render(request, 'mydoc.html', {
        'form': form
    })

def upload_profile(request):

    if request.method == 'POST':
        form = profileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('intro')
    else:
        form = profileForm()
    return render(request, 'profile.html', {
        'form': form
    })



def upload_Intro(request):

    if request.method == 'POST':
        form = IntroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info')
    else:
        form = IntroForm()
    return render(request, 'Intro.html', {
        'form': form
    })



def upload_me(request):

    if request.method == 'POST':
        form = AboutyouForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AboutyouForm()
    return render(request, 'aboutyou.html', {
        'form': form
    })



def upload_skills(request):

    if request.method == 'POST':
        form = skillsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aboutyou')
    else:
        form = skillsForm()
    return render(request, 'skills.html', {
        'form': form
    })

def upload_info(request):

    if request.method == 'POST':
        form = infoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doc' )
    else:
        form = infoForm()
    return render(request, 'info.html', {
        'form': form
    })

def register(response):
    form = UserCreationForm()
    return render(response,'register.html',{'form':form})

#def login(request):
    #return render(request,'login.html')


