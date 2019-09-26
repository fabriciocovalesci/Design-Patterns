# -*- coding:UTF-8 -*-
# calculador_de_impostos.py

'''
Strategy
Temos uma regra de negócio na qual os valores dos orçamentos 
podem ser submetidos a alguns impostos, como ISS, ICMS

'''
class Calculador_de_impostos(object):
    
    def realiza_calculo(self, orcamento):
        
        icms_calculado = orcamento.valor * 0.1
        print(icms_calculado)
        
if __name__ == "__main__":
    from orcamento import Orcamento
    
    orcamento = Orcamento(500.0)
    Calculador_de_impostos = Calculador_de_impostos()
    Calculador_de_impostos.realiza_calculo(orcamento)