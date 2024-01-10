from django.urls import path
from conversao.views import ConverterMoedaView

urlpatterns = [
    # Define a URL para a view ConverterMoedaView
    path('converter/', ConverterMoedaView.as_view(), name='converter_moeda'),
]
