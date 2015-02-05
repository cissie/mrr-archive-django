from django.contrib.auth.models import User
from django import forms
from library.models import *

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)


class EditForm(forms.ModelForm):
    record_label = forms.CharField(label="Label Name")
    catalog_number = forms.CharField(label="Catalog Number")
    release_year = forms.IntegerField(label="Release Year")
    issue_number = forms.IntegerField(label="Issue Number")
    reviewer_name = forms.CharField(label="Reviewer Name")
    record_review = forms.CharField(label="Add MRR Review")

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-2'
    helper.field_class = 'col-sm-4'
    helper.layout = Layout(
        Field('record_label', css_class='input-sm'),
        Field('catalog_number', css_class='input-sm'),
        Field('release_year', css_class='input-sm'),
        Field('issue_number', css_class='input-sm'),
        Field('reviewer_name', css_class='input-sm'),
        Field('record_review', css_class='input-sm'),
        FormActions(Submit('Save Changes', 'Save Changes', css_class='btn-primary'))
    )

    class Meta:
        model = User

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



