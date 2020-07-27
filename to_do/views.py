from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect
from .models import Todo , Last_Date
from .forms import TodoForm
from django.utils import timezone

from django import forms
from django.shortcuts import get_object_or_404
from django.http import HttpResponse,  Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone



def todo_view(request):
	form = TodoForm()
	all_todo = Todo.objects.all()
	pub_date = timezone.now()

	if request.method == 'POST':
		form = TodoForm(request.POST)
		if form.is_valid():
			form.save()

	context = {'form': form ,
			'all' : all_todo[::-1] ,
			'pub_date' : pub_date
		   }
	return render(request, 'to_do/todo.html', context)


def delete_todo(request, todo_id):
    item_to_delete = Todo.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')


def update_todo(request, pk) :
	all_todo = Todo.objects.get(id=pk)
	form = TodoForm(instance=all_todo)

	if request.method == 'POST':
		form = TodoForm(request.POST, instance=all_todo)
		if form.is_valid():
			form.save()
			return redirect('/todo/')

	context = {'form': form}
	return render(request, 'to_do/update.html', context)




# def todo_view(request) :
#     global todo_list
#     todo_list = []
#
#     all_todo = Todo.objects.all()
#     date = Last_Date.objects.all()
#
#     for do, date in zip(all_todo, date):
#         todo_list.append((do.todo, do.pub_date ,date.last_date ))
#
#     return render(request, 'to_do/todo.html',
#                   {'all': todo_list[::-1] })


# def todo_view(request) :
#     all_todo = Todo.objects.all()
#
#
#     return render(request, 'to_do/todo.html',
#                   {'all': all_todo[::-1] })


# def add_todo(request):
#     new_item = Todo(todo = request.POST['todo'])
#     new_date = Todo(last_date=request.POST['date'])
#
#     form = {
#       'new_item'    :  Todo(todo=request.POST['todo']) ,
#        'new_date'    :  Todo(last_date=request.POST['date']) }
#
#     form.save()
#     # new_item.save()
#     # new_date.save()
#
#     return HttpResponseRedirect('/todo/')