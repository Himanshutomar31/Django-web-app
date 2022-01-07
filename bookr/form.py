from django import forms

BOOK_CHOICES = (("Title", "Title"), ("Contributor", "Contributor"))

class SearchForm(forms.Form):
    search = forms.CharField(min_length=3, required=False)
    search_in = forms.ChoiceField(required=False, choices=BOOK_CHOICES)
