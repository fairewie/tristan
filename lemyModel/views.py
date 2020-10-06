from django.shortcuts import render, redirect
from django.forms import ModelForm , Textarea
from lemyModel.models import Task,User
from django import forms
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages

class TaskForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm , self).__init__(*args, **kwargs)
        self.fields['utilisateur'].label = "utilisateur "
        self.fields['task_name'].label = "Nom de tache"
        self.fields['release_date'].label = "date"
    class Meta:
        model = Task
        fields = ('utilisateur','task_name','release_date')


def La_Task(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            new_Task = form.save()
            messages.success(request,'Nouvelle Tache '+' '+new_Task.task_name + ' ' )
            context = {'pers': new_Task}
            return render(request,'detailfortask.html', context)
    context = {'form': form}
    return render(request,'Task.html', context)

def detailfortask(request,cid):
    Task = Task.objects.get(pk=cid)
    return HttpResponse('Nouvelle Tache '+Task.utilisateur+' '+Task.task_name)

class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm , self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "Prenom "
        self.fields['last_name'].label = "Nom"
    class Meta:
        model = User
        fields = ('first_name','last_name')


def Le_User(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_User = form.save()
            messages.success(request,'Nouvelle utilisateur '+new_User.first_name+' '+new_User.last_name)
            context = {'pers': new_User}
            return render(request,'detail.html', context)
    context = {'form': form}
    return render(request,'User.html', context)

def detail(request,cid):
    User = User.objects.get(pk=cid)
    return HttpResponse('Nouveau User'+User.first_name+' '+User.last_name)


def task_listing(request):
    objects = Task.objects.all().order_by('utilisateur')
    return render(request, template_name='list2.html',context={'objects': objects} )

def user_listing(request):
    objects = User.objects.all().order_by('first_name')
    return render(request, template_name='list.html',context={'objects': objects} )

def edit(request, param):
    pers = User.objects.get(pk=param)
    if request.method == "POST":
        form = UserForm(request.POST, instance=pers)
        if form.is_valid():
            form.save()
            messages.success(request, 'Personne '+pers.first_name+' modifiée!')
            context = {'pers': pers}
            return render(request,'detail.html',context)
    form = UserForm(instance=pers)
    context = {'form': form,'pers': pers}
    return render(request,'edite-crispy.html', context)

def taskedit(request, param):
    pers = Task.objects.get(pk=param)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=pers)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tache '+pers.task_name+' modifiée!')
            context = {'pers': pers}
            return render(request,'detailfortask.html',context)
    form = TaskForm(instance=pers)
    context = {'form': form,'pers': pers}
    return render(request,'taskedit.html', context)

def delete(request, pers_id):
    pers = User.objects.get(pk=pers_id)
    pers.delete()
    messages.success(request, "L'utilisateur "+pers.first_name+ " a était supprimée!")
    form = UserForm()
    context = {'form': form}
    return render(request, template_name='list.html',context={'objects': objects})

def deletetask(request, pers_id):
    pers = Task.objects.get(pk=pers_id)
    pers.delete()
    messages.success(request, 'La tache '+pers.task_name+" a était supprimée!")
    form = TaskForm()
    context = {'form': form}
    return render(request,template_name='list2.html', context={'objects': objects})
