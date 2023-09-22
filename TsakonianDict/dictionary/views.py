from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.shortcuts import redirect
from .models import Entry

# Create your views here.
 
def index(request):
    # Load the template
    template = loader.get_template("dictionary/index.html")

    # Set the context
    latest_entries = Entry.objects.order_by("tsakonian")
    text_to_show = """
Καούρ εκάνατε! Εγκείνι ενι το πρώκιου ηλεκτρονικό Τσακώνικο λεξικό!"""
    context = {
        "latest_entries": latest_entries,
        "text_to_show": text_to_show,
    }

    return HttpResponse(template.render(context, request))

def entry(request, entry):
    # Load the template
    template = loader.get_template("dictionary/entry.html")

    # Set the context
    entry = get_object_or_404(Entry, tsakonian=entry)
    tsakonian = entry
    greek = entry.greek

    context = {
        "tsakonian": tsakonian,
        "greek": greek,
    }

    return HttpResponse(template.render(context, request))

def invalid_entry(request, entry):
    # Load the template
    template = loader.get_template("dictionary/invalid_entry.html")

    # Set the context
    context = {
        "entry": entry,
    }

    return HttpResponse(template.render(context, request))

def search(request):
    # If the query is empty, redirect to the index page
    if not request.GET.get('q'):
        return redirect('/dictionary/')
    # Otherwise, check if the entry exists in the Entry model
    else:
        # Load the template
        template = loader.get_template("dictionary/search.html")

        # Set the context
        query = request.GET.get('q')
        entries = Entry.objects.filter(tsakonian__icontains=query)
        context = {
            "query": query,
            "entries": entries,
        }

        return HttpResponse(template.render(context, request))