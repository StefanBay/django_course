from django.shortcuts import render

from .models import Notes
from django.http import Http404, HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class NotesListView(LoginRequiredMixin,ListView):
    model = Notes
    context_object_name = "notes"
    template_name = 'notes/notes_list.html'
    login_url = "/login"

    def get_queryset(self):
        """Overwrites the super method, so that only the users own notes are returned"""
        return self.request.user.notes.all()

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'

from .forms import NotesForm
class NotesCreateView(CreateView):
    model = Notes
    #fields = ['title','text']
    success_url = '/smart/notes'
    form_class = NotesForm
    #template_name = 'notes/notes_form.html'

    def form_valid(self, form):
        """overwrite super method - the method writes the user who created the note. The model doesn't allow saving w/o suer, so it needs to be added. It injects the logged user in."""
        self.object = form.save(commit = False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'

# def list_notes(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html',{"notes" : all_notes})

# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk = pk)
#     except Notes.DoesNotExist:
#         raise Http404("ERROR: The note does not exist.")

#     return render(request,'notes/notes_detail.html', {"note": note})#{'title':note.title, 'text': note.text})