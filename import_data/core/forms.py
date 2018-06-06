from django import forms
from django.utils.translation import ugettext as _


class ImportarArquivoForm(forms.Form):
    arquivo = forms.FileField(label=_('Arquivo'))
