import random
substantivo = []
# NEW FEATURE !!!!!!!!!!!!!!!!!!!!!!
# OHHHHHHHHHHHHH MY GOOOOOOOOOODD !!!!!!!!!!!!!!
genero=''

while True:
 try:
  genero = str(input('Digite [M/F] para nickname masculino ou feminino: ')).strip().upper()

  if genero=='M':
    arquivo_1 = 'adjetivos_masc.txt'
    arquivo_2 = 'animais_masc.txt'
    break

  if genero=='F':
    arquivo_1 = 'adjetivos_fem.txt'
    arquivo_2 = 'animais_fem.txt'
    break

  else:
   print(f'gênero {genero} inválido')

 except Exception as e:
   print(f'Erro: {e}')

with open(arquivo_2,'r', encoding="utf-8") as file:
    for linhas in file:
        substantivo.append(linhas.strip())

# Embaralhar as listas para aumentar a aleatoriedade
random.shuffle(substantivo)
   


    
adjetivo= []

with open(arquivo_1,'r', encoding="utf-8") as file:
# Ler o conteúdo do arquivo
 for linhas in file:
    adjetivo.append(linhas.strip())

random.shuffle(adjetivo)



print(f"== 40 Nicknames épicos escolhidos aleatoriamente para você ==")
for i in range(1,41):
 subs_ale = random.choice(substantivo)
 adj_ale = random.choice(adjetivo)
 print(f'{i}º : {subs_ale} {adj_ale}')

