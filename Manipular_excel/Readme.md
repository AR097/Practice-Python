# Manipulação de Arquivos Excel com openpyxl

Este projeto utiliza a biblioteca `openpyxl` para ler e modificar arquivos Excel no formato `.xlsx`. O código carrega uma planilha existente, lê um valor de uma célula específica, modifica um valor em outra célula e, em seguida, salva as alterações em um novo arquivo.

## Pré-requisitos

Antes de executar o código, você precisa ter o Python instalado em seu sistema. Além disso, você deve instalar a biblioteca `openpyxl`. 

Você pode instalar a biblioteca usando o seguinte comando:

```bash
pip install openpyxl
```
## Arquivos Necessários
`dados.xlsx`: Este é o arquivo Excel que será carregado e modificado. Certifique-se de que este arquivo esteja no mesmo diretório que o script Python.

## Código
O seguinte código realiza as operações descritas:

python
```bash
from openpyxl import load_workbook

# Carregar o workbook existente
workbook = load_workbook(filename="dados.xlsx")
sheet = workbook.active

# Ler dados da célula A1
valor = sheet["A1"].value
print(f"Valor de A1: {valor}")

# Escrever um novo valor na célula B1
sheet["B1"] = "Novo Valor"

# Salvar as alterações
workbook.save("dados_atualizados.xlsx")
```
## Explicação do Código
Importação da Biblioteca: O código começa importando a função load_workbook da biblioteca openpyxl, que é usada para carregar arquivos Excel.

Carregar o Workbook: O arquivo dados.xlsx é carregado na variável workbook, e a planilha ativa é acessada através de sheet = workbook.active.

Leitura de Dados: O valor da célula A1 é lido e impresso no console.

Escrita de Dados: Um novo valor ("Novo Valor") é escrito na célula B1.

Salvar Alterações: As alterações são salvas em um novo arquivo chamado dados_atualizados.xlsx.

## Como Executar
Certifique-se de que o arquivo dados.xlsx esteja no mesmo diretório que o seu script Python.
Execute o script Python no terminal ou prompt de comando:

```bash
python seu_script.py
```
Substitua seu_script.py pelo nome do seu arquivo Python.


![image](https://github.com/user-attachments/assets/d381c151-7fc7-430c-9916-25deefa4844e)

![image](https://github.com/user-attachments/assets/e29de883-f420-4215-8f30-72cf81602fed)

![image](https://github.com/user-attachments/assets/d4551111-9f2c-4440-be0f-0b4975a675a2)

