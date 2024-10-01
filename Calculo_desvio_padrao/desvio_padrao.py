from statistics import pstdev

def calcular_desvio(numeros):
    desvio = pstdev(numeros)

    return desvio

def main():
    numeros = input("Digite uma lista de numeros separados por espaço: ")

    numeros = [float(numero) for numero in numeros.split()]

    desvio = calcular_desvio(numeros)

    print(f"Desvio padrão: {desvio}")

if __name__ == "__main__":
    main()