from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.


def login(request):
    if request.method == 'POST':
        return redirect('index')
    return render(request, 'login.html')

def index(request):
    return render(request, 'dashboard.html')