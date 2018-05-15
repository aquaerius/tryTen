from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'psychward/index.html', {'title':'Psych Ward', 'css':['/static/css/psychward.css',]})



