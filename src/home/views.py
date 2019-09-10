from django.shortcuts import render


#Defining the index view for home app
def index(request):
    return render(request, 'home/index.html', {'title':'Eskolare Book Catalog'})

def join(request):
    return render(request, 'home/join.html')

