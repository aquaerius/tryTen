from django.shortcuts import render


#Defining the index view for home app
def index(request):
  return render(request, 'home/index.html', {})
