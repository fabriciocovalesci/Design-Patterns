# -*- coding: UTF-8 -*-
# impostos.py

class INSS(object):

    def calcula(self, orcamento):
        return  orcamento.valor * 0.1

class ISS(object):
    
    def calcula(self, orcamento):
        return orcamento.valor * 0.06