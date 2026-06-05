from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def dogs(request):
    return render(request,'dogs.html')

def cats(request):
    return render(request,'cats.html')

def smallpets(request):
    return render(request,'smallpets.html')

def breed(request):
    return render(request,'breed.html')

def consultvet(request):
    return render(request,'consultvet.html')

def likes(request):
    return render(request,'likes.html')

def cart(request):
    return render(request,'cart.html')

def signin(request):
    return render(request,'signin.html')

def checkout(request):
    return render(request,'checkout.html')

def order(request):
    return render(request,'order.html')

def tracking(request):
    return render(request,'tracking.html')