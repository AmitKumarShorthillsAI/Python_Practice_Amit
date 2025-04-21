from django.shortcuts import render
import requests

FASTAPI_BASE_URL = "http://127.0.0.1:8000"

def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        res = requests.post(f"{FASTAPI_BASE_URL}/register", json={"username": username, "password": password})
        return render(request, "success.html", {"message": res.json()["message"]})
    return render(request, "register.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        res = requests.get(f"{FASTAPI_BASE_URL}/login", params={"username": username, "password": password})
        return render(request, "success.html", {"message": res.json()["message"]})
    return render(request, "login.html")
