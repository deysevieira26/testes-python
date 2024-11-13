# Criar a classe 
# chamada "CalculadoraIMC"
class CalculadoraIMC:
    def resultado (peso,altura):
        imc= peso / (altura * altura)
        if imc <19:
            return "magreza"
        elif imc >= >= 19 and imc < 24 :
            return "normal"
        elif >= 24 and imc < 29 :
            return "sobrepeso"
        else:
            return "obesidade"


