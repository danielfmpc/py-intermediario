op = 1
match op:
  case 1:
    print('opcao 1')
  case 2:
    print('opcao 2')
  case _:
    print('opcao invalida')

op = '1'
match op:
  case int(op):
    print('e int')
  case str(op):
    print('e string')
  case _:
    print('opcao invalida')

notas = {
  'Joao': 9,
  'Maria': 10,
  'Pedro': 8
}

match notas:
  case { 'Joao': 10 }:
    print('Joao tirou 10')
  case { 'Maria': _ }:
    print('Maria esta no dicionario')
  case _:
    print('Nenhuma informacao obtida')