from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def about_pfsa(request):
    """
    renders about page
    """
    return render(request, 'home/about_pfsa.html')
