conjunto_programacao = {'Ricardo', 'Roberto', 'Pedro', 'Vinicius'}
conjunto_futebol = { 'Mateus', 'Roberto', 'Paulo', 'Vinicius'}
conjunto_asimov = { 'Ricardo', 'Mateus', 'Paulo', 'Pedro' }

gostam_programacao_asimov = conjunto_programacao & conjunto_asimov
gostam_programacao_asimov

print('teste')

gostam_programacao_asimov_nao_futebol = gostam_programacao_asimov - conjunto_futebol
gostam_programacao_asimov_nao_futebol