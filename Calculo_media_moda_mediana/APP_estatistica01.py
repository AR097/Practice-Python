#importar as funçoes mean, median, mode da Bibilioteca statistics
from statistics import mean, median, mode

#<def> define uma função no python
#Nós definimos o nome da função (calcular_estatisticas)
#Nós definimos o nome da variável(numeros).  
def calcular_estatisticas(numeros):
    media = mean (numeros) #Aqui vai ser calculada a media
    mediana = median (numeros) #Aqui vai ser calculado o mediana

    try: #Ele permite que você evite que seu programa seja interrompido de maneira abrupta quando um erro ocorre. Em vez disso, você pode capturar o erro e tomar uma ação apropriada, como exibir uma mensagem de erro ou fornecer um valor alternativo.
        moda = mode(numeros) #busca a ocorrencia de moda
    except: #Se nao encontrar moda
        moda = "Nenhuma moda encontrada" #vai nos retornar essa mensagem.

    return media, mediana, moda #retornará os valores para nos

def main(): #vamos definir a função main
    #Aqui vamos definir que a variavel numeros é dada pelo usuario
    #Input é a função que permite que o usuario digite algo no console
    #.split() é um metodo de string que divide a string em uma lista, com base no delimitador padrao "espaço em branco". --- .split() transforma essa string em uma lista de strings: ['5', '10', '15', '20']
    numeros = input("Digite uma lista de numeros separados por espaço: ").split()

    #vamos converter casa numero de string para float(numeros decimais)
    #float(numero) converte cada string para um número decimal
    #for numero in numeros loop que percorre cada elemento da lista original numero
    numeros = [float(numero) for numero in numeros]

    media, mediana, moda = calcular_estatisticas(numeros)# Calcula a média, mediana e moda utilizando a função calcular_estatisticas

    print(f"Média: {media}") #Exibe os resultados para o usuário do valor media
    print(f"Mediana: {mediana}") #Exibe os resultados para o usuário do valor mediana
    print(f"Moda: {moda}")  #Exibe os resultados para o usuário do valor moda

# Se este script for executado diretamente, chama a função main()
if __name__ == "__main__":
    main()