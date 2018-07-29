from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Label, Note, Project
from django.views.decorators.http import require_http_methods
from django.utils import timezone


# Create your views here.
def index(request):
    notes = Note.objects.all()
    projects = Project.objects.all()
    # notes = []
    return render(request, 'notes/index.html', context={'notes': notes, 'projects': projects})


@require_http_methods(["POST"])
def add_note(request):
    try:
        note = Note(text=request.POST['new_note'],
                    project=Project.objects.get(pk=request.POST['project_id']),
                    date_added=timezone.now())
        note.save()
        text = 'Added a new note: %s (#%s)' % (note.text, note.id)
        print(text, note.project)
        return HttpResponse(text)
    except:
        return HttpResponse('Error', status=404)


def detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'notes/detail.html', context={'note': note})
