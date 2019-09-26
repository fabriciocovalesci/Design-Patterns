# -*- coding:UTF-8 -*-
# calculador_de_impostos.py

'''
Strategy
Temos uma regra de negócio na qual os valores dos orçamentos 
podem ser submetidos a alguns impostos, como ISS, ICMS

'''
from impostos import ISS, INSS

class Calculador_de_impostos(object):
    
    def realiza_calculo(self, orcamento, impostos):
        
        valor = impostos.calcula(orcamento)
        print(valor)
        
if __name__ == "__main__":
    from orcamento import Orcamento
    from impostos import INSS, ISS
    
    orcamento = Orcamento(500.0)
    print("\nImposto de INSS ")
    calculador_de_impostos = Calculador_de_impostos()
    calculador_de_impostos.realiza_calculo(orcamento, INSS())
    print("\nImposto de ISS ")
    calculador_de_impostos.realiza_calculo(orcamento, ISS())
  