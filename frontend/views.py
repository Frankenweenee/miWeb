from django.shortcuts import render

# Create your views here.



def home(request):
    return render(request,'frontend/index.html')

def portfolio(request):
    return render(request, "frontend/works.html")

def about(request):
    return render(request,'frontend/about.html')


def work(request):
    return render(request,'frontend/work.html')

