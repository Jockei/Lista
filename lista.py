import numpy as np # Biblioteca numpy
import matplotlib.pyplot as plot # Biblioteca matplotlib

'''
1. Crie um array NumPy contendo os números de 1 a 10. Em seguida,
transforme-o em um array bidimensional com 2 linhas e 5 colunas.
'''

# 1
print("Questão 1")
matriz_1 = np.arange(1, 11).reshape(2, 5) # Criar matriz 2x5 com os numeros de 1 a 10
print(matriz_1)
print()

'''
2. Crie dois arrays de tamanho 10 contendo números aleatórios entre 1 e 100.
Some, subtraia, multiplique e divida os dois arrays.
'''

#2
print("Questão 2")
array_1 = np.random.randint(1, 101, 10) # Criar um array de 1x10 com os numeros de 1 a 100 aleatoriamente
array_2 = np.random.randint(1, 101, 10) # Criar um array de 1x10 com os numeros de 1 a 100 aleatoriamente
print(array_1)
print(array_2)

print(array_1 + array_2) # somar os dois arrays
print(array_1 - array_2) # subitrair os dois arrays
print(array_1 * array_2) # multiplicar os dois arrays
print(array_1 / array_2) # dividir os dois arrays
print()

'''
7. Crie um array bidimensional representando notas de 5 alunos em 4 provas.
Calcule a média de cada aluno e a média de cada prova.
'''

#7
print("Questão 7")
array_prova = np.random.randint(1, 11, 20).reshape(5, 4) # Criar um array de 5x4 com os numeros de 1 a 10 aleatoriamente
print(array_prova)

media_aluno = np.mean(array_prova, axis=1) # Calcular a media de cada linha
print(media_aluno)

media_prova = np.mean(array_prova, axis=0) # Calacular a media de cada coluna
print(media_prova)
print()

'''
17.Crie uma matriz quadrada 3×3 aleatória. Calcule o determinante e, se
possível, a inversa dessa matriz.
'''

#17
print("Questão 17")
matiz_quadrada = np.random.randint(1, 11, 9).reshape(3, 3) # Criar um array de 3x3 com os numeros de 1 a 10 aleatoriamente
print(matiz_quadrada)

det_matiz_quadrada = np.linalg.det(matiz_quadrada) # Calcular o determinante da matriz
print(det_matiz_quadrada)

if det_matiz_quadrada == 0: # Verificar se o determinante é diferente de 0
  print("A matriz não tem inversa")

else:
  inversa_matiz_quadrada = np.linalg.inv(matiz_quadrada) # Calcular a inversa da matriz
  print(inversa_matiz_quadrada)
print()

'''
23.Crie um array contendo números inteiros de 1 a 20. Substitua todos os
números que são divisíveis por 3 por -3.
'''

#23
print("Questão 23")
array_inteiros = np.arange(1, 21)
print(array_inteiros)

array_inteiros[array_inteiros % 3 == 0] = -3
print(array_inteiros)
print()

'''
24.Crie uma matriz 5×5 contendo os números inteiros de 1 a 25. Extraia a
submatriz formada pelas linhas 2 a 4 e pelas colunas 2 a 4.
'''

#24
print("Questão 24")
matriz_inteiros = np.arange(1, 26).reshape(5, 5) # Criar uma matriz de 5x5 com os numeros de 1 a 25
print(matriz_inteiros)

sub_matriz = matriz_inteiros[1:4, 1:4] # extrair uma submatriz formada pelas linha 2 a 4 e coluna 2 a 4
print(sub_matriz)
print()

'''
27.Crie uma matriz 2×2 para representar uma transformação linear e um vetor
v=[1,2]. Aplique a transformação ao vetor v multiplicando-o pela matriz.
'''

#27
print("Questão 27")
matriz_transformacao = np.array([[1, 2], [3, 4]]) # cria uma matriz 2x2 com os numeros 1, 2, 3 e 4
vetor_v = np.array([1, 2]) # Cria um vetor com os numeros 1 e 2
print(matriz_transformacao)
print(vetor_v)

vetor_transformado = np.dot(matriz_transformacao, vetor_v) # Multiplicando uma matriz e um vetor
print(vetor_transformado)
print()

'''
28.Dado o array x=[0,1,2,3,4] e y=[1,2,0,2,1], crie novos valores para xxx em
passos de 0.1 usando numpy.interp. Plote os valores interpolados (se
necessário, use Matplotlib para exibir).
'''

#28
print("Questão 28")
x = [0,1,2,3,4]
y = [1,2,0,2,1]
xxx = np.arange(0, 4.1, 0.1) # Ele vai fazer todo o seguimento de x só que ao passo de 0.1
yyy = np.interp(xxx, x, y)
print(xxx)
print(yyy)
plot.plot(x, y, 'o', label='Original data')
plot.plot(xxx, yyy, '-', label='Interpolated data')
plot.legend()
plot.xlabel('x')
plot.ylabel('y')
plot.title('Interpolação de dados')
plot.show()
print()
