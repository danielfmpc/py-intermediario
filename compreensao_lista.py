valores = list(range(10))

maiores_que_5 = []

for valor in valores:
  if valor > 5:
    maiores_que_5.append(valor)

print(maiores_que_5)

def somar_dois_ao_quadrado(valor):
  return valor ** 2 + 2

maiores_que_5 = [somar_dois_ao_quadrado(valor) for valor in valores if valor > 5]
maiores_que_5