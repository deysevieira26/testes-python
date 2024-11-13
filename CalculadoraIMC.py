# Criar a classe 
# chamada "CalculadoraIMC"
class CalculadoraIMC:
    def resultado (self,peso,altura):
        imc= peso / (altura * altura)
        if imc <19:
            return "magreza"
        elif imc >= 19 and imc < 24 :
            return "normal"
        elif imc >= 24 and imc < 29 :
            return "sobrepeso"
        else:
            return "obesidade"
        


