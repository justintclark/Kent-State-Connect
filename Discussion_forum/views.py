from django.shortcuts import render,redirect
from .models import * 
from .forms import * 
# Create your views here.

def home(request):
    forums=forum.objects.all()
    count=forums.count()
    context={'forums':forums,
            'count':count}
    return render(request,'home.html', context)

def addInForum(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request,'addInForum.html',context)

def addInDiscussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request,'addInDiscussion.html',context)

def GeneralDiscussions(request):
    forums=forum.objects.all()
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'GeneralDiscussions.html', context)

def ClassDiscussions(request):
    forums=forum.objects.all()
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())

    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'ClassDiscussions.html', context)

def TutoringDiscussions(request):
    forums=forum.objects.all()
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())
    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request, 'TutoringDiscussions.html', context)