# -*- coding:UTF-8 -*-

class Calcula_descontos(object):
    
    def calcula(self, orcamento):
        
        if orcamento.total_itens > 5:
            return orcamento.valor * 0.1
        
        elif orcamento.valor > 500:
            return orcamento.valor * 0.07
        

if __name__ =="main":
    