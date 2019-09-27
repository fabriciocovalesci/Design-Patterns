# -*- coding: UTF-8 -*-
# calculador_de_impostos.py

"""
Quando temos diferentes algoritmos que possuem estruturas parecidas, 
o Template Method é uma boa solução. Com ele conseguimos definir em um nível
mais macro a estrutura do algoritmo, deixando "buracos" que serão implementados 
de maneira diferente por cada uma das implementações específicas.
"""

class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):
        valor = imposto.calcula(orcamento)
        print (valor)

if __name__ == '__main__':

    from orcamento import Orcamento, Item

    # adicionado os impostos no import
    from impostos import ISS, ICPP, IKCV, INSS

    orcamento = Orcamento()
    # adicionando itens ao orçamento
    orcamento.adiciona_item(Item('ITEM 1', 50))
    orcamento.adiciona_item(Item('ITEM 2', 200))
    orcamento.adiciona_item(Item('ITEM 3', 250))

    calculador_de_impostos = Calculador_de_impostos()
    print ('ISS e ICMS')
    calculador_de_impostos.realiza_calculo(orcamento, ISS())
    calculador_de_impostos.realiza_calculo(orcamento, INSS())

    # cálculo dos novos impostos
    print ('ICPP e IKCV')
    calculador_de_impostos.realiza_calculo(orcamento, ICPP()) # imprime 25.0
    calculador_de_impostos.realiza_calculo(orcamento, IKCV()) # imprime 30.0