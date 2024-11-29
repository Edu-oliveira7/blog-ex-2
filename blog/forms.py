from django import forms


class Mensagemform(forms.Form):
    nome = forms.CharField(
        max_length=100,
        widget=forms.Textarea(attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    telefone = forms.CharField(
        max_length=12,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    cidade = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    mensagem = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={"class": "form-control"})
    )
