palavras = ['Olá', 'Python', 'Juliano', 'Asimov Acadamy']

dict_caracteres = { 
  palavra: len(palavra.replace(' ', ''))
  for palavra  in palavras
}

dict_caracteres
