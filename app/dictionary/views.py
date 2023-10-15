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
    tsakonian = entry

    try:
        entry = get_object_or_404(Entry, tsakonian = tsakonian)
        greek = entry.greek
    except:
        greek = "Δεν βρέθηκε η λέξη στο λεξικό."

    context = {
        "tsakonian": tsakonian,
        "greek": greek,
    }

    return HttpResponse(template.render(context, request))

def tsakonian(request, entry):
    # Load the template
    template = loader.get_template("dictionary/tsakonian.html")

    # Set the context
    tsakonian_ = entry

    # Search for entries that contain the Greek word in the Greek column
    results = Entry.objects.filter(tsakonian = tsakonian_)

    # If there are results, build a list with the following format:
    # i. Greek word
    if results:
       greek_list = [entry for entry in results]
    
    # Otherwise, return an empty list
    else:
        greek_list = []
    
    context = {
        "tsakonian" : tsakonian_,
        "greek_list": greek_list,
    }

    return HttpResponse(template.render(context, request))

def greek(request, entry):
    # Load the template
    template = loader.get_template("dictionary/greek.html")

    # Set the context
    greek = entry

    # Search for entries that contain the Greek word in the Greek column
    reverse_results = Entry.objects.filter(greek__icontains = greek)

    # If there are results, build a list with the following format:
    # Tsakonian word — Greek word
    if reverse_results:
       tsakonian_list = [f'{entry.tsakonian} — {entry.greek}' for entry in reverse_results]
    
    # Otherwise, return an empty list
    else:
        tsakonian_list = []
    
    context = {
        "greek": greek,
        "tsakonian_list": tsakonian_list,
    }

    return HttpResponse(template.render(context, request))

        
def search(request):
    # If the request is empty, go back to the main page
    query = request.GET.get('q')
    direction = request.GET.get('direction')
    print(direction)

    if not request.GET.get('q'):
        return redirect('/dictionary/')
    
    # Otherwise, redirect to the entry page
    else:
        return redirect(f'/dictionary/{direction}/{query}')