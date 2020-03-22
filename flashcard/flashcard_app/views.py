from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'flashcard_app/home.html',{})

def addition(request):
    return render(request,'flashcard_app/addition.html',{})

def subtraction(request):
    return render(request,'flashcard_app/subtraction.html',{})

def multiplication(request):
    return render(request,'flashcard_app/multiplication.html',{})

def division(request):
    return render(request,'flashcard_app/division.html',{})