# -*- coding:UTF-8 -*-
"""
Esses descontos formam como se fosse uma "corrente", ou seja, um ligado ao outro. 
Daí o nome do padrão de projeto: Chain of Responsibility. 
A ideia do padrão é resolver problemas como esses: de acordo com o cenário, 
devemos realizar alguma ação. Ao invés de escrevermos código procedural, 
e deixarmos um único método descobrir o que deve ser feito, quebramos essas 
responsabilidades em várias diferentes classes, e as unimos como uma corrente.
"""

from desconto import Desconto_por_cinco_itens, Desconto_por_mais_quinhentos_reais, Sem_desconto

class Calcula_descontos(object):
    
    def calcula(self, orcamento):
        
        desconto = Desconto_por_cinco_itens(
            Desconto_por_mais_quinhentos_reais(Sem_desconto())
            ).calcula(orcamento)
        
        return desconto

if __name__ == "__main__":

    from orcamento import Orcamento, Item
    
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM - 1', 100))
    orcamento.adiciona_item(Item('ITEM - 2',  50)) 
    orcamento.adiciona_item(Item('ITEM - 3', 500))
    orcamento.adiciona_item(Item('ITEM - 4', 400))
    
    calculador = Calcula_descontos()
    desconto = calculador.calcula(orcamento)
    
    print(f"Desconto calculado R$ {desconto}")