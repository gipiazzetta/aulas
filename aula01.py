## funções matemáticas básicas
# + soma
# - subtrair
# * multiplicar
# / dividir
## ** exponenciação

# () utilizado para funções
# [] utilizado para listas
# {} utilizado para dicionarios ou para a função de concatenar textos no print
# f"{} utilizado para concatenar

## função para imprimir um texto
print("funciona")

## criar variaveis
str_works = "funciona" # string
salario = 3000  # int
boleto = 265.67 # float
poupanca = 10000 #int
bool_works = True

print(str_works)
print(salario)
print(bool_works)
print(salario + poupanca - boleto)

# type diz o tipo da variável
print(type(bool_works))

# Criar listas []
frutas = ["maca", "banana", "melancia"]

print(frutas)

# Incluir coisas na lista .append ou .insert. No insert tem que colocar a posição que quer incluir.
## Lembrar que sempre começa da posição 0.
frutas.append("apple")
print(frutas)
frutas.insert(1,"abacaxi")
print(frutas)

## Descobrir o tamanho da lista = len
print(len(frutas))

# Descobrir qual fruta está na posição x
print(frutas[3])

# Descobrir quais frutas até chegar na posição X, colocar ":" antes da posição
print(frutas[:3])

# Descobrir quais frutas estão da posição X em diante, colocar ":" depois da posição
print(frutas[3:])

# Descobrir frutas de um determinado range
print(frutas[2:4])

#if, else - utilizado para fazer condições. Não esquecer ":". Um bloco condicional
##sempre começa if e termina com else. Não pode ter mais de um if e um else no mesmo
## bloco
alt = 30
gi = 29

if gi < alt:
    print("gi é mais nova que o alt")
else:
    print("gi é mais velha que o alt")

# Elif condições que ficam entre if e else. Podem ser ilimitadas condições
if gi < alt:
    print("gi é mais nova que o alt")
elif gi == alt:
    print("gi tem a mesma idade que o alt")
else:
    print("gi é mais velha que o alt")

# Identação = Tab. Python só funciona com identação. Ex: espaço antes do print.

# loop = for. SEMPRE PRECISA DE UMA LISTA.
## Utilizado para realizar operações em listas.

lista_supermercado = [8.90, 9.00, 24.00, 45.00]
total = 0
for item_da_lista in lista_supermercado:
    total = total + item_da_lista
    print(total)

print(total)

# zip = gera tuplas/triplas/etc (pares/trios/etc) de listas e o loop faz a iteração dessas listas

# zip tupla
lista_itens_supermercado   = ["banana","maca","carne","vinho"]
lista_valores_supermercado = [8.90, 9.00, 24.00, 45.00]

for item_da_lista, valor_item in zip(lista_itens_supermercado,lista_valores_supermercado):
    print(f"{item_da_lista} --> {valor_item}")

# zip tripla
lista_itens_supermercado   = ["banana","maca","carne","vinho"]
lista_valores_supermercado = [8.90, 9.00, 24.00, 45.00]
status = ["barato", "barato", "caro", "caro"]

for item_da_lista, valor_item, item_status in zip(lista_itens_supermercado,lista_valores_supermercado,status):
    print(f"{item_da_lista} --> {valor_item} --> {item_status}")

# zip com if
for item_da_lista, valor_item, item_status in zip(lista_itens_supermercado,lista_valores_supermercado,status):
    if item_status == "caro":
        print(f"{item_da_lista} está {item_status}")
    else:
        print(f"{item_da_lista} está {item_status}")
