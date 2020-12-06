'''
  Consoantes - Obstruinte
  Sonorização X Dessonorização

  Receives an incorrect word, returns a dictionary in the form
  word_rule_dict.update({
    "misspelled_word": sample_str,
    "target_word": sample_str_correct,
    "error_category": category_x_x,
    "POS": POS,
    "syllabic_separation": syllables,
    "vowel_meeting":  ditongo/None,
    "cvs_encoding": CV encoding,
  })
  if the word is found, else return None
'''

#-----------------------------------------------------------------------------
#Files, libs and packages needed

'''
  Importing modules from parent folder
  https://stackoverflow.com/a/33532002/7162336
'''
from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
# import my_module  # Replace "my_module" here with the module name.
from validate_target_word import *
from change_letters import *
sys.path.pop(0)

# Regex
import re

#-----------------------------------------------------------------------------

category_6_1 = "Consoante – Obstruinte: Sonorização"
category_6_2 = "Consoante – Obstruinte: Dessonorização"

def category_6(sample_str):
  sample_str = sample_str.lower()
  category = ''
  word_rule_dict = {}
  possible_corrections = []

  #padrões regex
  lista_padroes_surdas = [
                          '\a*qu\a*', '\a*sc\a*', '\a*sç\a*', '\a*ss\a*',
                          '\a*xs\a*', '\a*xc\a*', '\a*ch\a*',
                          '\a*p\a*', '\a*t\a*', '\a*f\a*',
                          '\a*s\a*', '\a*z\a*', '\a*c\a*', '\a*ç\a*', '\a*x\a*',
                        ]

  lista_padroes_sonoras = [
                  '\a*b\a*', '\a*d\a*', '\a*gu\a*', '\a*g\a*', '\a*v\a*', '\a*z\a*',
                  '\a*s\a*', '\a*x\a*', '\a*j\a*', '\a*g\a*']

  # lista de padrões
  lista_surdas = '(?:% s)' % '|'.join(lista_padroes_surdas)
  lista_sonoras = '(?:% s)' % '|'.join(lista_padroes_sonoras)


  #CATEGORY 7_1
  #Sonorização surda é grafada como sonora
  #para a correção procurar na lista de sonoras, trocar por surda

  sample_str_copy = sample_str #cópia de segurança da palavra original
  # acha todos as consoantes que se encaixam na lista de 'sonoras'
  consoantes_sonoras_encontradas = re.findall(lista_sonoras, sample_str_copy)
  if(consoantes_sonoras_encontradas):
    # indexes onde deve ser trocada a letra
    cs_indexes = [(m.span()) for m in re.finditer(lista_sonoras, sample_str)]
    for indexes in cs_indexes:
      s, e = indexes

      # /b/ <b> | b -> p
      if(sample_str_copy[s:e] == 'b'):
        # substituição do padrão
        sample_str_correct = change_letters(sample_str_copy, sample_str_copy[s:e], s, e, 'p')
        #procura a palavra, se existir retorna obj com informacoes
        word_rule_dict = validate_target_word(sample_str_copy, sample_str_correct)
        if(word_rule_dict):
          word_rule_dict.update({
            "error_category": category_6_1,
          })
          # salva nas possiveis correções
          possible_corrections.append(word_rule_dict)
        else:
          sample_str_correct = ''

      # /d/ <d> | d -> t
      if(sample_str_copy[s:e] == 'd'):
        # substituição do padrão
        sample_str_correct = change_letters(sample_str_copy, sample_str_copy[s:e], s, e, 't')

        #procura a palavra, se existir retorna obj com informacoes
        word_rule_dict = validate_target_word(sample_str_copy, sample_str_correct)
        if(word_rule_dict):
          word_rule_dict.update({
            "error_category": category_6_1,
          })
          # salva nas possiveis correções
          possible_corrections.append(word_rule_dict)
        else:
          sample_str_correct = ''

      # /g/ <g> <gu> troca por: /k/ <c> <qu>
      if(sample_str_copy[s:e] == 'gu' or sample_str_copy[s:e] == 'g'):
        grafias_k = ['qu', 'c',]
        for c in grafias_k:
          sample_str_correct = change_letters(sample_str_copy, sample_str_copy[s:e], s, e, c)
          #procura a palavra, se existir retorna obj com informacoes
          word_rule_dict = validate_target_word(sample_str_copy, sample_str_correct)
          if(word_rule_dict):
            word_rule_dict.update({
              "error_category": category_6_1,
            })
            # salva nas possiveis correções
            possible_corrections.append(word_rule_dict)
          else:
            sample_str_correct = ''

      # /v/ <v> | v -> f
      if(sample_str_copy[s:e] == 'v'):
        sample_str_correct = change_letters(sample_str_copy, sample_str_copy[s:e], s, e, 'f')
        #procura a palavra, se existir retorna obj com informacoes
        word_rule_dict = validate_target_word(sample_str_copy, sample_str_correct)
        if(word_rule_dict):
          word_rule_dict.update({
            "error_category": category_6_1,
          })
          # salva nas possiveis correções
          possible_corrections.append(word_rule_dict)
        else:
          sample_str_correct = ''

      # **Apenas no começo
      # procurar por /z/ <z> <s> <x> | trocar para /s/ <s> <z> <c/ç> <x> <sc/sç> <ss> <xs> <xc> 
      if(
        (
          sample_str_copy[s:e] == 'z' or 
          sample_str_copy[s:e] == 's' or 
          sample_str_copy[s:e] == 'x'
        ) and
        s == 0
      ):
        grafias_s = ['s', 'z', 'c', 'ç', 'x', 'sc', 'sç', 'ss', 'xs', 'xc']
        for c in grafias_s:
          sample_str_correct = change_letters(sample_str_copy, sample_str_copy[s:e], s, e, c)
          #procura a palavra, se existir retorna obj com informacoes
          word_rule_dict = validate_target_word(sample_str_copy, sample_str_correct)
          if(word_rule_dict):
            word_rule_dict.update({
              "error_category": category_6_1,
            })
            # salva nas possiveis correções
            possible_corrections.append(word_rule_dict)
          else:
            sample_str_correct = ''

      # /ʒ/ <j> <g> | troca para /ʃ/ <x> <ch>
      if(sample_str_copy[s:e] == 'j' or sample_str_copy[s:e] =='g'):
        # /ʃ/ Fricativa pós-alveolar surda
        grafias_fpas = ['ch', 'x']
        for c in grafias_fpas:
          sample_str_correct = change_letters(sample_str_copy, sample_str_copy[s:e], s, e, c)
          #procura a palavra, se existir retorna obj com informacoes
          word_rule_dict = validate_target_word(sample_str_copy, sample_str_correct)
          if(word_rule_dict):
            word_rule_dict.update({
              "error_category": category_6_1,
            })
            # salva nas possiveis correções
            possible_corrections.append(word_rule_dict)
          else:
            sample_str_correct = ''

  #CATEGORY 7_2
  # Dessonorização, sonora é grafada como surda
  # para a correção procurar na lista de surda, trocar por sonora
  sample_str_copy = sample_str #cópia de segurança da palavra original
  # acha todos as consoantes que se encaixam na lista de 'surdas'
  consoantes_surdas_encontradas = re.findall(lista_surdas, sample_str)

  if(consoantes_surdas_encontradas):
    # indexes onde deve ser trocada a letra
    cs_indexes = [(m.span()) for m in re.finditer(lista_surdas, sample_str)]

    for indexes in cs_indexes:
      word_rule_dict = {}
      s, e = indexes

      # /s/ -> /z/
      if(
        (sample_str_copy[s:e] == 's' or
        sample_str_copy[s:e] == 'z' or
        sample_str_copy[s:e] == 'c' or
        sample_str_copy[s:e] == 'ç' or
        sample_str_copy[s:e] == 'x' or
        sample_str_copy[s:e] == 'sc' or
        sample_str_copy[s:e] == 'sç' or
        sample_str_copy[s:e] == 'ss' or
        sample_str_copy[s:e] == 'xs' or
        sample_str_copy[s:e] == 'xc')
        and s == 0
      ):
        grafias_z = [ 'z', 's', 'x']
        for c in grafias_z:
          sample_str_correct = change_letters(sample_str_copy, sample_str_copy[s:e], s, e, c)
          #procura a palavra, se existir retorna obj com informacoes
          word_rule_dict = validate_target_word(sample_str_copy, sample_str_correct)
          if(word_rule_dict):
            word_rule_dict.update({
              "error_category": category_6_2,
            })
            # salva nas possiveis correções
            possible_corrections.append(word_rule_dict)
          else:
            sample_str_correct = ''

      # /p/ <p> | p -> b
      if(sample_str_copy[s:e] == 'p'):
        # substituição do padrão
        sample_str_correct = change_letters(sample_str_copy, sample_str_copy[s:e], s, e, 'b')
        #procura a palavra, se existir retorna obj com informacoes
        word_rule_dict = validate_target_word(sample_str_copy, sample_str_correct)
        if(word_rule_dict):
          word_rule_dict.update({
            "error_category": category_6_2,
          })
          # salva nas possiveis correções
          possible_corrections.append(word_rule_dict)
        else:
          sample_str_correct = ''

      #/t/ -> /d/
      if(sample_str_copy[s:e] == 't'):
        sample_str_correct = change_letters(sample_str_copy, sample_str_copy[s:e], s, e, 'd')
        #procura a palavra, se existir retorna obj com informacoes
        word_rule_dict = validate_target_word(sample_str_copy, sample_str_correct)
        if(word_rule_dict):
          word_rule_dict.update({
            "error_category": category_6_2,
          })
          # salva nas possiveis correções
          possible_corrections.append(word_rule_dict)
        else:
          sample_str_correct = ''

      #/k/ -> /g/ | <c> <qu> -> <g> <gu> ->
      if(sample_str_copy[s:e] == 'qu' or sample_str_copy[s:e] == 'c'):
        grafias_k = ['gu', 'g',]
        for c in grafias_k:
          sample_str_correct = change_letters(sample_str_copy, sample_str_copy[s:e], s, e, c)
          #procura a palavra, se existir retorna obj com informacoes
          word_rule_dict = validate_target_word(sample_str_copy, sample_str_correct)
          if(word_rule_dict):
            word_rule_dict.update({
              "error_category": category_6_2,
            })
            # salva nas possiveis correções
            possible_corrections.append(word_rule_dict)
          else:
            sample_str_correct = ''

      # /f/ -> /v/
      if(sample_str_copy[s:e] == 'f'):
        sample_str_correct = change_letters(sample_str_copy, sample_str_copy[s:e], s, e, 'v')
        #procura a palavra, se existir retorna obj com informacoes
        word_rule_dict = validate_target_word(sample_str_copy, sample_str_correct)
        if(word_rule_dict):
          word_rule_dict.update({
            "error_category": category_6_2,
          })
          # salva nas possiveis correções
          possible_corrections.append(word_rule_dict)
        else:
          sample_str_correct = ''

      # /ʃ/ -> /ʒ/
      if(sample_str_copy[s:e] == 'ch' or sample_str_copy[s:e] =='x'):
        # /ʃ/ Fricativa pós-alveolar surda
        grafias_fpas = ['j', 'g']
        for c in grafias_fpas:
          sample_str_correct = change_letters(sample_str_copy, sample_str_copy[s:e], s, e, c)
          #procura a palavra, se existir retorna obj com informacoes
          word_rule_dict = validate_target_word(sample_str_copy, sample_str_correct)
          if(word_rule_dict):
            word_rule_dict.update({
              "error_category": category_6_2,
            })
            # salva nas possiveis correções
            possible_corrections.append(word_rule_dict)
          else:
            sample_str_correct = ''

  if(possible_corrections != []):
    return possible_corrections
  else:
    return None


# Tests - Status = OK
# teste = category_6("fes") #fez
# teste = category_6("ensima") #Não deve ser corrigida
# if(teste): 
#   for item in teste:
#     print(item)
# else:
#   print('Não foi corrigida pela categoria')