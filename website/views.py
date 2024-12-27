from ast import Add
from email.headerregistry import Address
from re import S
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    #check to see of logging in
    records = Record.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #authenticate user
        user = authenticate(request,username=username, password=password)

        #check if user is not None
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.error(request, "Error logging in - please try again")
            return redirect('home')
    else:
        return render(request, 'website/home.html', {'records':records})

#def login_user(request):
    #pass


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            

   #authenticate usera and log in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user =authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'website/register.html', {'form':form})

    return render(request, 'website/register.html', {'form':form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        #get the record
       customer_record = Record.objects.get(id=pk)
       return render(request, 'website/record.html', {'customer_record':customer_record})

    else:
        messages.error(request, "Please log in to view customer records")
        return redirect('home')


    #record delete function

def delete_record(request, pk):
    if request.user.is_authenticated:
        #get the record
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request, "Record deleted")
        return redirect('home')
    else:
        messages.error(request, "Please log in to delete customer records")
        return redirect('home')
    
    #return render(request, 'website/record.html', {'customer_record':customer_record

def add_record(request):
    form = AddRecordForm(request.POST or None)

    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                #add_record.user = request.user
                #add_record.save()
                messages.success(request, "Record added successfully")
                return redirect('home')

        return render(request, 'website/add_record.html', {'form':form})
    else:
        messages.error(request, "Please log in to add customer records")
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        #if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully")
            return redirect('home')
        return render(request, 'website/update_record.html', {'form':form})
    else:
        messages.error(request, "Please log in to update customer records")
        return redirect('home')