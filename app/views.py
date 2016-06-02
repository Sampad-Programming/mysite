from django.shortcuts import render

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
# Create your views here.
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )
def time(request):
    """Renders the server time."""
    p = str(datetime.now())
    o = p.split()
    y = o[1].split(".")
    return HttpResponse(y[0])

def forum(request,path):
    """Renders the forum page."""

    return HttpResponse("Not Available YET")
    """
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Forum Page',
            'year':datetime.now().year,
        })
    )"""
def blog(request, path):
    """Renders the blog page."""

    return HttpResponse("Not Available YET")
    """
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Blog Page',
            'year':datetime.now().year,
        })
    )"""