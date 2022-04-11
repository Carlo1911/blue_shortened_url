from django import forms


class TransformerUrlForm(forms.Form):
    url = forms.URLField()
