def peso_peixe():
    pesoLimite = 50
    peso = float(input("Digite a quantidade de kgs de peixe que João trouxe: "))
    if peso > pesoLimite:
        excesso = peso - pesoLimite
        multa = excesso * 4.00
        print("Multa foi de", multa, "reais")
peso_peixe()
