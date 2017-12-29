from django import forms

from oo.meta.models import Type, Instance


class TypeForm(forms.ModelForm):

    class Meta:
        model = Type
        exclude = []


class InstanceForm(forms.ModelForm):

    role = forms.ChoiceField(
        choices=Instance.ITEM_ROLES,
        initial=Instance.THING
    )

    identifiers = forms.CharField()

    class Meta:
        model = Instance
        exclude = []
