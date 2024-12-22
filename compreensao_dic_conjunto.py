valores = list(range(10))

#compreensao de tuplas
maiores_que_5 = {valor for valor in valores if valor > 5}
maiores_que_5

#compreensao dicionario
valores_em_dolares = {
  'leite': 0.78,
  'arroz': 4.60,
  'feijao': 0.35,
}

fator_conversao = 6.30

valores_em_rais ={
  chave: round(valor * fator_conversao, 2)
  for chave, valor in valores_em_dolares.items()
}
valores_em_rais

