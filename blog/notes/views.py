from django.shortcuts import render
from .models import Note


def notes_index(request):
    notes = Note.objects.all().order_by('date')
    return render(request, 'notes_index.html', {'notes': notes})
