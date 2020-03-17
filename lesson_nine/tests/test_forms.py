from django.test import TestCase

from lesson_nine import forms


class SearchFormTest(TestCase):

    def test_renew_form_date_field_label(self):
        form = forms.SearchForm()
        self.assertEqual(form.fields['search_field'].help_text, 'Write some request')

