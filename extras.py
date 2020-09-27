## criar função
pi = 30
pd = 40

def junta_numeros(v1,v2):
    return float(f"{v1}.{v2}")

valor_total = junta_numeros(pi,pd)

print(valor_total)


## metodo imutável
def metodo(p1, p2):
    px =  p1.copy()
    px.append(p2)
    return px

x  = "uva"

frutas2 = metodo(frutas, x)
print(frutas2)
print(frutas)
