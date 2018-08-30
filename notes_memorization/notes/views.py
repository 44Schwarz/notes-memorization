from random import randint
import csv
from lxml import etree

from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.http.response import HttpResponseRedirect

from .models import Label, Note, Project
from django.views.decorators.http import require_http_methods
from django.utils import timezone


# Create your views here.
def index(request):
    notes = Note.objects.all()
    projects = Project.objects.all()
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
        return HttpResponseRedirect('/notes')
    except:
        return HttpResponse('Error', status=404)


def detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'notes/detail.html', context={'note': note})


@require_http_methods(["GET"])
def review(request):
    id_list = [n.id for n in Note.objects.all()]
    cur_id = request.GET.get('cur_id')
    if cur_id:  # get next note
        if id_list.index(int(cur_id)) == len(id_list) - 1:
            num = id_list[0]  # if the previous note was the last in list, get the first one
        else:
            num = id_list[id_list.index(int(cur_id)) + 1]
        obj = Note.objects.get(pk=num)
        obj.reviews_counter += 1
        obj.save()
        return JsonResponse({'note': str(obj), 'note_id': obj.id})
    else:  # get random note
        num = id_list[randint(0, len(id_list) - 1)]
        obj = Note.objects.get(pk=num)
        obj.reviews_counter += 1
        obj.save()
        return render(request, 'notes/review.html', context={'note': obj})


def download(request):
    try:
        notes = Note.objects.all()
        if request.GET.get('type') == 'csv':
            with open('notes.csv', 'w') as f:
                note_writer = csv.writer(f)
                note_writer.writerow(['ID', 'Text', 'Project', 'Date added', '# of reviews', 'Url', 'File'])
                for note in notes:
                    note_writer.writerow([note.id, note.text, note.project, note.date_added,
                                          note.reviews_counter, note.link_url, note.link_file])

        elif request.GET.get('type') == 'xml':
            root = etree.Element('notes')

            for note in notes:
                n = etree.SubElement(root, 'note')

                for attr in ('id', 'text', 'project', 'date_added', 'reviews_counter', 'link_url', 'link_file'):
                    etree.SubElement(n, attr).text = str(note.__getattribute__(attr))

            etree.ElementTree(root).write('notes.xml', pretty_print=True, xml_declaration=True, encoding='UTF-8')
    except Exception as e:
        return JsonResponse({'result': e})
    else:
        return JsonResponse({'result': True})
