from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.views import generic
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

# class IndexView(generic.ListView):
#     template_name = "dictionary/index.html"
#     context_object_name = "latest_entries"

#     def get_queryset(self):
#         """Return the last five published entries."""
#         return Entry.objects.order_by("tsakonian")
    
# class EntryView(generic.DetailView):
#     model = Entry
#     template_name = "dictionary/entry.html"
