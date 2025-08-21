from django.test import TestCase
from django.urls import reverse
from .models import Note

# Create your tests here.


class NoteTests(TestCase):
    def test_create_note(self):
        response = self.client.post(reverse('note_create'), {
            'title': 'Test Note',
            'content': 'This is a test.'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 1)

    def test_list_notes(self):
        Note.objects.create(title="Note 1", content="Content 1")
        response = self.client.get(reverse('note_list'))
        self.assertContains(response, "Note 1")

    def test_update_note(self):
        note = Note.objects.create(title="Old", content=" Old Content")
        response = self.client.post(reverse('note_update', args=[note.id]), {
            'title': 'Updated',
            'content': 'Updated content'})
        self.assertEqual(response.status_code, 302)
        note.refresh_from_db()
        self.assertEqual(note.title, 'Updated')

    def test_delete_note(self):
        note = Note.objects.create(title="Delete Me", content=" Remove this")
        response = self.client.post(reverse('note_delete', args=[note.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 0)
