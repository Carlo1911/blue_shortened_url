from django.http import HttpRequest
from django.test import TestCase

from .forms import TransformerUrlForm


class TestTransformerUrl(TestCase):
    def setUp(self):
        self.req = HttpRequest()
        self.req.POST["url"] = "https://www.google.com/"

    def test_empty_form(self):
        form = TransformerUrlForm()
        fields = ["url"]
        for field in fields:
            self.assertIn(field, form.fields)

    def test_form_ok(self):
        form = TransformerUrlForm(self.req.POST)
        self.assertTrue(form.is_valid())
