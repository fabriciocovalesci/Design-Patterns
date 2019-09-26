# -*- codeing: UTF-8 -*-
#orcamento.py

class Orcamento(object):
    def __init__(self, valor):
        self.__valor = valor
        
    @property    
    def valor(self):
        """Criamos o atributo valor como property, encapsulando , sendo possivel ser acessado apenas como leitura"""
        return self.__valor