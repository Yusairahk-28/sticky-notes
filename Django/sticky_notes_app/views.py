from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


def note_list(request):
    # Retrieves all Note objects from the database.
    notes = Note.objects.all()
    # Prepares data to be passed to the template.
    context = {
        "notes": notes,
        "page_title": "List of Notes"
    }
    # Renders the note list template with context.
    return render(request, 'notes/note_list.html', context)


# Retrieves and renders the note.
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/note_form.html', {'note': note})


# Checks if the form was submitted and validate the form data
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})


# Attempt to get the Note object.
def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)
    # Checks if form is valid.
    if request.method == 'POST':
        form = NoteForm(request.POST or None, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})


# Function to delete note.
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('note_list')
