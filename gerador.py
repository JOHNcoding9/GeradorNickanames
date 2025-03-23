import random
substantivo = []
arquivo = 'substantivo.txt'

with open(arquivo,'r', encoding="utf-8") as file:
    for linhas in file:
        substantivo.append(linhas.strip())

# Embaralhar as listas para aumentar a aleatoriedade
random.shuffle(substantivo)

genero=''

while True:
 try:
  genero = str(input('Digite [M/F] para nickname masculino ou feminino: ')).strip().upper()

  if genero=='M':
    arquivo = 'adjetivos_masc.txt'
    break

  if genero=='F':
    arquivo = 'adjetivos_fem.txt'
    break

  print(f'gênero {genero} inválido')

 except Exception as e:
   print(f'Erro: {e}')
   


    
adjetivo= []

with open(arquivo,'r', encoding="utf-8") as file:
# Ler o conteúdo do arquivo
 for linhas in file:
    adjetivo.append(linhas.strip())

random.shuffle(adjetivo)



print(f"== 35 Nicknames épicos escolhidos aleatoriamente para você ==")
for i in range(1,36):
 subs_ale = random.choice(substantivo)
 adj_ale = random.choice(adjetivo)
 print(f'{i}º : {subs_ale} {adj_ale}')

