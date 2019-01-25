from django import forms

from .models import Function

class FunctionForm(forms.ModelForm):
    """Form definition for Function."""

    class Meta:
        """Meta definition for Functionform."""

        model = Function
        fields = ('name', 'content', 'comment', 'tags')
