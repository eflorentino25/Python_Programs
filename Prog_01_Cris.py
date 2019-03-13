# CRISTINA CARNEIRO RIBEIRO
# 1. Nota será igual a soma da multiplicação dos pesos pelos seus atributos
# 2. Caso o candidato tenha escrito mais de 10 artigos, então o peso de artigo sobe para 2
# 3. Caso o candidato zere em algum atributo então a nota final dele será 0
# 
# Pesos:
# xp: 5
# cursos: 2
# artigos: 1

PESO_XP = 5
PESO_CURSO = 2
PESO_ART = 1
P_ART10 = 2

def calcula_nota(candidato):
  if candidato['xp'] ==0 or candidato['cursos']==0 or candidato['artigos']==0:
    # return 0
    nota = 0
  	 
  if candidato['artigos'] >10:
   		nota = (candidato['xp']*PESO_XP)+ (candidato ['cursos'] *PESO_CURSO)+(candidato['artigos']*P_ART10)
  else
      nota = (candidato['xp']*PESO_XP)+ (candidato ['cursos'] *PESO_CURSO)+(candidato['artigos']*PESO_ART)
  
    
  
  return nota


# $ pytest
# test_calcula_nota.py



def test_deve_retornar_8_quando_todos_os_atributos_forem_1():
  candidato = {
    'xp': 1,
    'cursos': 1,
    'artigos': 1
  }
  assert calcula_nota(candidato) == 8
  
def test_mais_10_artigos ():
  candidato = {
    'xp': 1,
    'cursos': 1,
    'artigos': 11
  }
  assert calcula_nota (candidato) == 29

  
def test_atritbuto_zero():
  candidato = {
    'xp':0,
    'curso':1,
    'artigos': 1
  }
  assert calcula_nota(candidato) == 0
