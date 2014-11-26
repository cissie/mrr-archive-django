from django import forms
from library.models import Artist, RecordTitle

class ArtistForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the artist name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Artist

class RecordTitleForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the record title.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = RecordTitle

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        fields = ('title', 'url', 'views')
