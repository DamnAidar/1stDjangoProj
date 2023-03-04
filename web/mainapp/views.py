from django.shortcuts import render



def index(request):
    return render(request, 'mainapp/index.html')


def about(request):
    return render(request, 'mainapp/page2.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')


def wtf(request):
    return render(request, 'mainapp/wtf.html')
