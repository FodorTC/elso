from django.shortcuts import render

def index(request):
    template='index.html'
    context={}
    return render(request, template, context)

# Create your views here.
