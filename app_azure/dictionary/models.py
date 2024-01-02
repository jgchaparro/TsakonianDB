from django.db import models

# Create your models here.
class Source(models.Model):
    title = models.CharField(max_length=300)
    name = models.CharField(max_length=50, blank=True)
    surname = models.CharField(max_length=50, blank=True)
    year = models.IntegerField(blank=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return f'{self.surname}, {self.name} ({self.year}) - {self.title}'

class Entry(models.Model):
    tsakonian = models.CharField(max_length=50, primary_key=True)
    greek = models.CharField(max_length=200)
    paradigm = models.CharField(max_length=5)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    notes = models.CharField(max_length=30, blank=True, null=True)
    
    def __str__(self):
        return self.tsakonian