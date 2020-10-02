## 1 -  crie 3 variaveis (númerica, string e booleana)

## 2 - crie uma lista de animais, adicione um animal e remova um animal da lista.
## Use o google para verificar como se remove um item da lista

## 3 - com a lista de animais criada no exercicio anterior, crie uma nova lista de tamanho dos animais e percorra os animais utilizando
## o zip e o loop for .

## imprima somente os animais que sao grandes utilizando o if / else:

## RESPOSTA 01
altura = 160
nome = "giovana"
amorzinho = True

print(altura)
print(nome)
print(amorzinho)

## RESPOSTA 2
animais = ["gato", "preguiça", "cachorro", "panda"]

print(animais)

##RESPOSTA 2A
animais.append("cavalo")

print(animais)

##RESPOSTA 2B
del(animais[2])

print(animais)

## RESPOTA 3A

peso = ["3kg", "6kg", "25kg", "78kg"]
porte = ["pequeno", "médio", "grande", "grande"]

for item_animais, item_peso, item_porte in zip(animais, peso, porte):
    print(f"{item_animais} --> {item_peso} --> {item_porte}")

##RESPOSTA 3B
for item_animais, item_peso, item_porte in zip(animais, peso, porte):
    if item_porte == "grande":
        print(f"{item_animais} pesa {item_peso}. Por isso é considerado {item_porte} porte")
