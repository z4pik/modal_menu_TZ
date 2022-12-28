from django import forms
from menu.models import MenuItem


class MenuItemForm(forms.ModelForm):
    """Форма для создания меню"""
    class Meta:
        model = MenuItem
        fields = ['name', 'parent', 'explicit_url', 'named_url']

    def clean_explicit_url(self):
        return self.cleaned_data['explicit_url'] or None

    def clean_named_url(self):
        return self.cleaned_data['named_url'] or None
