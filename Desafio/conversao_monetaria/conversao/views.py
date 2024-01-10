from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .forms import ConversaoMoedaForm
from .models import Moeda

class ConverterMoedaView(View):
    def get(self, request):
        # Cria uma instância do formulário com os dados da requisição GET
        form = ConversaoMoedaForm(request.GET)
        
        # Verifica se o formulário é válido
        if form.is_valid():
            # Obtém os dados do formulário
            from_moeda = form.cleaned_data['from_moeda']
            to_moeda = form.cleaned_data['to_moeda']
            amount = form.cleaned_data['amount']

            try:
                # Busca no banco de dados as moedas de origem e destino
                moeda_origem = Moeda.objects.get(nome=from_moeda)
                moeda_destino = Moeda.objects.get(nome=to_moeda)
            except Moeda.DoesNotExist:
                # Retorna um erro caso uma das moedas não seja encontrada
                return JsonResponse({'error': 'Moeda não encontrada'}, status=400)

            # Realiza a conversão
            converted_amount = amount * (moeda_destino.cotacao / moeda_origem.cotacao)

            # Retorna o resultado da conversão em JSON
            return JsonResponse({'result': converted_amount})

        # Renderiza o formulário na página se não for válido
        return render(request, 'converter_moeda.html', {'form': form})
