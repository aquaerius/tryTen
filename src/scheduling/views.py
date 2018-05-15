from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
def service_list(request):
    return render(request, 'scheduling/service_list.html', {})


def owners_detail(request):
    return render(request, 'scheduling/owners_detail.html', {})


def contractors_detail(request):
    return render(request, 'scheduling/contractors_detail.html', {})



