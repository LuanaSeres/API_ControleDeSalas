from django import forms

class ReservaForm(forms.Form):
    dataInicio = forms.DateTimeField(label='Data de Início', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    dataFim = forms.DateTimeField(label='Data de Fim', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    motivo = forms.CharField(label='Motivo', widget=forms.TextInput(attrs={'placeholder': 'Motivo da reserva'}))
