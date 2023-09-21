from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
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

def word(request, word):
    # entry = Entry.objects.get(tsakonian=word)
    # Recreate this line, but with get_object_or_404
    entry = get_object_or_404(Entry, tsakonian=word)
    # Extract the Greek translation from the database
    greek = entry.greek
    return HttpResponse(f"You're looking at word {word}. Translation: {greek}.")

