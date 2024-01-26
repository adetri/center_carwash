from django.shortcuts import render

# Create your views here.


def regis_check(request):
    if request.method == 'POST':
        data = {}
