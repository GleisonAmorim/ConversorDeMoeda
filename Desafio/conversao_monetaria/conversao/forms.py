from django import forms

class ConversaoMoedaForm(forms.Form):
    # Campo para a moeda de origem
    from_moeda = forms.CharField(label='De Moeda', max_length=3)
    # Campo para a moeda de destino
    to_moeda = forms.CharField(label='Para Moeda', max_length=3)
    # Campo para a quantidade a ser convertida
    amount = forms.DecimalField(label='Quantidade')
