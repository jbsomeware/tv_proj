from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show
# Create your views here.
def index(request):
    
    return redirect('/shows')

def show_list(request):
    context = {
        "show_list": Show.objects.all()
    }
    return render(request, "tv_show_app/all_shows.html", context)

def add_new_show(request):
    
    return render(request, "tv_show_app/add_new_show.html")

def create(request):
    if request.method == "POST":
        errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/shows/new')
    else:
        Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'],)
    new=Show.objects.last()
    print(request.POST['release_date'])
    
    return redirect(f'/shows/{new.id}')

def show_info(request, val):
    context = {
        "show_info": Show.objects.get(id=val),
    }
    return render(request, "tv_show_app/info_show.html", context)

def show_edit(request, val):
    context = {
        "show_info": Show.objects.get(id=val),
    }
    return render(request, "tv_show_app/edit_show.html", context)

def show_update(request, val):
    if request.method == "POST":
        errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(f'/shows/{val}/edit')
    else:
        u=Show.objects.get(id=val)
        u.title=request.POST['title']
        u.network=request.POST['network']
        u.release_date=request.POST['release_date']
        u.description=request.POST['description']
        u.save()
        messages.success(request, "Show successfully updated")
    return redirect(f'/shows/{val}')

def show_delete(request, val):
    if request.method == "POST":
        u=Show.objects.get(id=val)
        u.delete()
    
    return redirect('/shows')