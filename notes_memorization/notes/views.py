from django.shortcuts import render
from django.http import HttpResponse
from .models import Label, Note, Project
from django.views.decorators.http import require_http_methods


# Create your views here.
def index(request):
    notes = Note.objects.all()
    # notes = []
    return render(request, 'notes/index.html', context={'notes': notes})


@require_http_methods(["POST"])
def add_note(request):
    print('Added a new note: %s' % request.POST['new_note'])  # TODO
    return HttpResponse()
