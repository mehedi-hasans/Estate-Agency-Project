from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def agent(request):
    return render(request, 'agent-single.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def agents(request):
    return render(request, 'agents-grid.html')

def blog(request):
    return render(request, 'blog-grid.html')

def blogSingle(request):
    return render(request, 'blog-single.html')

def property(request):
    return render(request, 'property-grid.html')

def propertySingle(request):
    return render(request, 'property-single.html')


