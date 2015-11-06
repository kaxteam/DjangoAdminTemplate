from django.http import HttpResponse
from django.shortcuts import render, redirect

def root(request):
    return redirect("/panel")

def panel(request):
    return render(request, "pages/dashboard.html")
