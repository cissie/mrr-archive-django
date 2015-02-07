from django.contrib.auth.models import User
from django import forms
from django.core.urlresolvers import reverse
from library.models import *

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

# Crispy form to allow users to edit certain fields
class EditForm(forms.ModelForm):
    record_label = forms.ModelChoiceField(queryset=RecordLabel.objects.all(), label="Label Name")
    catalog_number = forms.CharField(label="Catalog Number")
    release_year = forms.IntegerField(label="Release Year")
    issue_number = forms.IntegerField(label="Issue Number")
    reviewer_name = forms.CharField(label="Reviewer Name")
    record_review = forms.CharField(label="Add MRR Review", widget=forms.Textarea())

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-2'
    helper.field_class = 'col-sm-4'
    # helper.form_action = reverse('record_title_detail')
    helper.layout = Layout(
        # Div('record_label', 'catalog_number', 'release_year', 'issue_number', 'reviewer_name', 'record_review'),
        Field('record_label', css_class='input-sm'),
        Field('catalog_number', css_class='input-sm'),
        Field('release_year', css_class='input-sm', max_length=4),
        Field('issue_number', css_class='input-sm', max_length=3),
        Field('reviewer_name', css_class='input-sm'),
        Field('record_review', css_class='input-sm'),
        FormActions(Submit('Save Changes', 'Save Changes', css_class='btn-primary'))
    )

    class Meta:
        model = RecordTitle
        fields = (
            'record_label',
            'catalog_number',
            'release_year',
            'issue_number',
            'reviewer_name',
            'record_review',
        )

        def __init__(self, *args, **kwargs):
            super(EditForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper(self)
            # self.helper.form_action = reverse('record_title_detail', args=['record_title.id'])

            return super(EditForm, self).__init__(*args, **kwargs)


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


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')


# class ImageUploadForm(forms.Form):
#     """Image upload form."""
#     image = forms.ImageField()



