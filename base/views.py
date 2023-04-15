from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'base/home.html')


def Contact(request):
    return render(request, 'base/contact.html')