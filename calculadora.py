# Criar a classe 
# chamada "Calculadora"
class Calculadora:

    # 1) Criar o método
    # chamado "soma()"
    def soma(self, n1 , n2):
        return n1 + n2
    
    # 2) Criar o método 
    # chamado "subtracao"
    def subtracao(self, n1, n2):
        return n1 - n2
    
     # 3) Criar o método 
    # chamado "multiplicacao"
    def multiplicacao(self, n1, n2):
        return n1 * n2
    
     # 4) Criar o método 
    # chamado "divisao"
    def divisao(self, n1, n2):
       # return n1 / n2
       if n2 == 0:
            return "Divisão inválida"
       else:
           return n1 / n2