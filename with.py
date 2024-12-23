# arquivo = open('arquivo.txt', 'w')
# arquivo.write('Olá, mundo!')
# arquivo.close()


with open('arquivo.txt', 'w') as arquivo:
  arquivo.write('Olá, mundo!2')


import tempfile

with tempfile.TemporaryDirectory() as directory:
  print(f'Diretório temporario criado em {directory}')

