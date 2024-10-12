'''
1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?
'''
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
  K = K + 1
  SOMA = SOMA + K
  print(SOMA)

# 1-R: 91

'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
'''

def calcula_sequencia_fibonacci(numero):
    if numero == 0:
        return "O valor 0 é da sequência Fibonacci."
    elif numero == 1:
        return "O valor 1 é da sequência Fibonacci."
    else:
        sequencia = [0, 1]
        
        while True:
            proximo_valor = sequencia[-1] + sequencia[-2]
            
            if proximo_valor > numero:
                break
            
            sequencia.append(proximo_valor)
        
        return "O valor " + str(numero) + " é da sequência Fibonacci." if numero in sequencia else "O valor " + str(numero) + " não é da sequência Fibonacci."

numero = int(input("Digite um número para verificar se ele pertence à sequência de Fibonacci: "))
print(calcula_sequencia_fibonacci(numero))

'''
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.
'''

faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total_faturamento = sum(faturamento.values())

for estado, valor in faturamento.items():
  percentual = round((valor / total_faturamento) * 100, 2)
  print(f"Estado: {estado}, Faturamento R${valor:.2f}, Percentual de Representação: {percentual}%")

'''
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
'''

def inverter_string(string):
    nova_lista = []
    
    for indice in range(len(string)-1, -1, -1):
        nova_lista.append(string[indice])
    
    return "".join(nova_lista)


string_definida = "João é brasileiro"
print("A string definida é: ", string_definida)
print("A string invertida é: ", inverter_string(string_definida))

entrada_usuario = input("Insira uma string para que seja invertida: ")
print("Você inseriu a seguinte string:", entrada_usuario)
print("A string invertida é: ", inverter_string(entrada_usuario))

