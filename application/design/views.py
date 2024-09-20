from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def demo_form(request):
    return render(request, 'examples/form.html')