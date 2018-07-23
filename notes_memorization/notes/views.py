from django.shortcuts import render
from django.http import HttpResponse
from .models import Label, Note, Project
from django.views.decorators.http import require_http_methods
from django.utils import timezone


# Create your views here.
def index(request):
    notes = Note.objects.all()
    # notes = []
    return render(request, 'notes/index.html', context={'notes': notes})


@require_http_methods(["POST"])
def add_note(request):
    try:
        note = Note(text=request.POST['new_note'], project=Project.objects.get(pk=1), date_added=timezone.now())
        note.save()
        text = 'Added a new note: %s (#%s)' % (note.text, note.id)
        print(text)
        return HttpResponse(text)
    except:
        return HttpResponse('Error', status=404)
